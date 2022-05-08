# Volatility-and-Dependence-Modelling
Modelling volatility for financial time series. Copulas are used to create multivariate distributions of financial assets. Based on labs in Financial Risk Management at Liu.

## Volatility Modelling

The aim is to find good models for returns of financial assets. In doing so, I look at common methods to model volatility which are extensivley used practice. The models examined are 

* EqWMA
* EWMA 
* GARCH(1,1) 

These are also tested visually using QQ-plots and ECDFS. Other stylized facts are also examined for the return distributions.

## Dependency Modelling
 
When modelling multiple financial assets the dependency between the assets must be considered. In order to do this a multivariate distribution is required. This is done by using copulas in conjunction with the univariate distributions found in the eariler volatility modelling part. 

Using copulas we are able to simulate future returns, and thus prices, of financial assets with a correct dependency strucutre. In this part we look at **NOK/USD** and **EUR/USD**.

# Risk-Assessment-and-Backtesting
Risk Modelling with Value at Risk using different approaches, such as historical simulation, Extreme Value Theory and risk-factor mapping. Based on labs in Financial Risk Management at Liu.
