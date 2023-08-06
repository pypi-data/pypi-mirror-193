from . import cov_matrix
from . import simulation 
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import norm, t
from statsmodels.tsa.arima.model import ARIMA
from scipy.optimize import minimize 

# Calculate the return
def return_calculate(prices, method="DISCRETE", dateColumn="Date"):
    vars_ = prices.columns
    nVars = len(vars_)
    vars_ = [var for var in vars_ if var != dateColumn]
    if nVars == len(vars_):
        raise ValueError(f"dateColumn: {dateColumn} not in DataFrame: {vars_}")
    nVars = nVars - 1

    p = prices[vars_].to_numpy()
    n, m = p.shape
    p2 = np.empty((n-1, m))

    for i in range(n-1):
        for j in range(m):
            p2[i, j] = p[i+1, j] / p[i, j]

    if method.upper() == "DISCRETE":
        p2 = p2 - 1.0
    elif method.upper() == "LOG":
        p2 = np.log(p2)
    else:
        raise ValueError(f"method: {method} must be in (\"LOG\",\"DISCRETE\")")

    dates = prices[dateColumn].iloc[1:n].to_numpy()
    out = pd.DataFrame({dateColumn: dates})
    for i in range(nVars):
        out[vars_[i]] = p2[:, i]

    return out

# Calculate ES
def calculate_es(data, var):
  return -np.mean(data[data <= -var])

# Calculate Var
def calculate_var(data, mean=0, alpha=0.05):
  return mean - np.quantile(data, alpha)

# Normal distribution
def calculate_var_normal(returns, num_simulations=10000, alpha=0.05):
    """Calculate VaR using a normal distribution"""
    mu = returns.mean()
    sigma = returns.std()
    sim_returns = np.random.normal(mu, sigma, num_simulations)
    sim_returns.sort()
    var_normal = -sim_returns[int(alpha * len(sim_returns))]
    es_normal = calculate_es(sim_returns,var_normal)
    return var_normal, es_normal, sim_returns

# Normal distribution with an Exponentially Weighted variance (λ = 0. 94)
def calculate_var_ew_normal(returns, lambda_=0.94, num_simulations=10000, alpha=0.05):
    """Calculate VaR using a normal distribution with exponentially weighted variance"""
    mu = returns.mean()
    sigma = np.sqrt(cov_matrix.exp_weighted_cov(returns, lambda_=lambda_))
    sim_returns = np.random.normal(mu, sigma[0][0], num_simulations)
    var_ew = -np.percentile(sim_returns, alpha*100)
    es_ew = calculate_es(sim_returns,var_ew)
    return var_ew, es_ew, sim_returns

# MLE fitted T distribution
def MLE_T(params, returns):
    negLL = -1 * np.sum(t.logpdf(returns, df=params[0], loc=params[1], scale=params[2]))
    return(negLL)

def calculate_var_t_MLE(returns, num_simulations=10000, alpha=0.05):
    """Calculate VaR using a T-distribution with MLE fitted degrees of freedom"""
    constraints=({"type":"ineq", "fun":lambda x: x[0]-1}, {"type":"ineq", "fun":lambda x: x[2]})
    returns_t = minimize(MLE_T, x0=[10, np.mean(returns), np.std(returns)], args=returns, constraints=constraints)
    df, loc, scale = returns_t.x[0], returns_t.x[1], returns_t.x[2]
    sim_returns = t.rvs(df, loc=loc, scale=scale, size=num_simulations)
    var_t = -np.percentile(sim_returns, alpha*100)
    es_t = calculate_es(sim_returns,var_t)
    return var_t, es_t, sim_returns

# AR(1)
def calculate_var_ar1(returns, num_simulations=10000, alpha=0.05):
    """Calculate VaR using an AR(1) model"""
    model = ARIMA(returns, order=(1, 0, 0)).fit()
    alpha_1 = model.params[0]
    beta = model.params[1]
    resid = model.resid
    sigma = np.std(resid)
    sim_returns = np.empty(num_simulations)
    returns = returns.values
    for i in range(num_simulations):
        sim_returns[i] = alpha_1 * returns[-1] + sigma * np.random.normal()
    var_ar1 = -np.percentile(sim_returns, alpha*100)
    es_ar1 = calculate_es(sim_returns,var_ar1)
    return var_ar1, es_ar1, sim_returns

# Historic
def calculate_var_hist(returns, alpha=0.05):
    """Calculate VaR using historic simulation"""
    var_hist = -np.percentile(returns, alpha*100)
    es_hist = calculate_es(returns,var_hist)
    return var_hist, es_hist, returns


### Portfolio

def get_portfolio_price(portfolio, prices, portfolio_code, Delta=False):
    """Get the price for each asset in portfolio and calculate the current price."""
    
    if portfolio_code == "All":
        assets = portfolio.drop('Portfolio',axis=1)
        assets = assets.groupby(["Stock"], as_index=False)["Holding"].sum()
    else:
        assets = portfolio[portfolio["Portfolio"] == portfolio_code]
        
    stock_codes = list(assets["Stock"])
    assets_prices = pd.concat([prices["Date"], prices[stock_codes]], axis=1)
    
    current_price = np.dot(prices[assets["Stock"]].tail(1), assets["Holding"])
    holdings = assets["Holding"]
    
    if Delta == True:
        asset_values = assets["Holding"].values.reshape(-1, 1) * prices[assets["Stock"]].tail(1).T.values
        delta = asset_values / current_price
        
        return current_price, assets_prices, delta
    
    return current_price, assets_prices, holdings

def calculate_delta_var(portfolio, prices, alpha=0.05, lambda_=0.94, portfolio_code="All"):
    """
    Calculate delta VaR for a given portfolio using the Delta Normal VaR method.
    
    Parameters:
    - portfolio: a pandas DataFrame with columns 'Portfolio', 'Stock', and 'Holding'
    - prices: a pandas DataFrame with columns 'Date' and stock codes as column names
    - alpha: the significance level for VaR calculation, default 0.05
    - lambda_: fraction for update the covariance matrix, default 0.94
    - portfolio_code: a string for the specific portfolio to calculate, default "All"
    
    Returns:
    - current_value: current value for the specific portfolio
    - VaR: delta VaR for the portfolio in $
    """
    
    current_price, assets_prices, delta = get_portfolio_price(portfolio, prices, portfolio_code, Delta=True)

    returns = return_calculate(assets_prices).drop('Date', axis=1)
    assets_cov = cov_matrix.exp_weighted_cov(returns, lambda_)

    p_sig = np.sqrt(np.transpose(delta) @ assets_cov @ delta)
    
    var_delta = -current_price * norm.ppf(alpha) * p_sig
    
    return current_price[0], var_delta[0][0]

def calculate_MC_var(portfolio, prices, alpha=0.05, lambda_=0.94, n_simulation = 10000, portfolio_code="All"):
    """
    Calculate delta VaR for a given portfolio using the Delta Normal VaR method.
    
    Parameters:
    - portfolio: a pandas DataFrame with columns 'Portfolio', 'Stock', and 'Holding'
    - prices: a pandas DataFrame with columns 'Date' and stock codes as column names
    - alpha: the significance level for VaR calculation, default 0.05
    - lambda_: fraction for update the covariance matrix, default 0.94
    - portfolio_code: a string for the specific portfolio to calculate, default "All"
    
    Returns:
    - current_value: current value for the specific portfolio
    - VaR: delta VaR for the portfolio in $
    """
    
    current_price, assets_prices, holdings = get_portfolio_price(portfolio, prices, portfolio_code)
    
    returns = return_calculate(assets_prices).drop('Date',axis=1)
    returns_norm = returns - returns.mean()
    assets_cov = cov_matrix.exp_weighted_cov(returns_norm, lambda_)
    
    assets_prices = assets_prices.drop('Date',axis=1)
    np.random.seed(0)
    sim_returns = np.add(simulation.multivariate_normal_simulation(assets_cov, n_simulation, method='pca'), returns.mean().values)
    sim_prices = np.dot(sim_returns* assets_prices.tail(1).values.reshape(assets_prices.shape[1],),holdings)
    
    var_MC = -np.percentile(sim_prices, alpha*100)
    es_MC = calculate_es(sim_prices,var_MC)
    return current_price[0], var_MC, es_MC, sim_prices

def calculate_historic_var(portfolio, prices, alpha=0.05,n_simulation=1000, portfolio_code="All"):
    """
    Calculate historical Value at Risk (VaR) for a given portfolio using exponentially weighted covariance.

    Parameters:
    - portfolio: a pandas DataFrame of the portfolio with columns "Portfolio", "Stock", "Holding"
    - prices: a pandas DataFrame of historical prices with columns "Date" and stock codes as other columns
    - alpha: a float between 0 and 1 for the confidence level, default 0.05
    - portfolio_code: a string for the specific portfolio to calculate, default "All"

    Returns:
    - historic_var: a float for the historical VaR in $
    """
    
    current_price, assets_prices, holdings = get_portfolio_price(portfolio, prices, portfolio_code)
    
    returns = return_calculate(assets_prices).drop("Date", axis=1)
    
    assets_prices = assets_prices.drop('Date',axis=1)
    sim_returns = returns.sample(n_simulation, replace=True)
    sim_prices = np.dot(sim_returns* assets_prices.tail(1).values.reshape(assets_prices.shape[1],),holdings)
    
    var_hist = -np.percentile(sim_prices, alpha*100)
    es_hist = calculate_es(sim_prices,var_hist)
    
    return current_price[0], var_hist, es_hist, sim_prices