# Volatility-and-Dependence-Modelling
Modelling volatility with EqWMA, EWMA and GARCH models for financial time series. Copulas are used multivariate distributions of financial assets. Based on labs in Financial Risk Management at Liu.

## Volatility Modelling

The aim is to find good models for returns of financial assets. In doing so, I look at different ways to model volatility which is used extensivley in return modelling. The models examined are the EqWMA, EWMA and GARCH(1,1) models. These are also tested visually using QQ-plots and ECDFS. Other stylized facts are also examined for the return distributions.

## Dependency Modelling
 
When modelling multiple financial assets the dependency between the assets must be considered. In order to do this we need a multivariate model of the assets. This is done by using copulae in conjunction with the univariate distributions found in the eariler volatility modelling part. This makes it possible to simulate future returns, and thus prices, of financial assets with a correct dependency strucutre. In this part we look at **NOK/USD** and **EUR/USD**.