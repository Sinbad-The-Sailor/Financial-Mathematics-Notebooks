from pandas_datareader import data as pdr
import numpy as np
from scipy.optimize import minimize

snp500_weekly = pdr.get_data_yahoo("^GSPC", start="2011-12-28", end="2021-12-28", interval="wk")
snp500_weekly = snp500_weekly['Adj Close']
aud_weekly = pdr.get_data_yahoo("AUDUSD=X", start="2011-12-28", end="2021-12-28", interval="wk")
aud_weekly = aud_weekly['Adj Close']

# Log return calculation
snp500_weekly_returns = np.log(snp500_weekly/snp500_weekly.shift(1))
aud_weekly_returns = np.log(aud_weekly/aud_weekly.shift(1))

# Average returns 
aud_average_return = aud_weekly_returns.mean() * 365/7 * 100
snp500_average_return = snp500_weekly_returns.mean() * 365/7 * 100

def loglikelihood(lamb: float) -> float:
    sum = 0
    for i in range(len(snp500_weekly_returns)):
        sum = sum - np.log(5)
    return sum
