# Financial Mathematics Notebooks
Notebooks containing examples and labs of matematical finance. 

### Volatility Modelling

Three different volatility models are examined for the return processes of financial assets. The models examined are given below with a corresponding volatility plot over time.

* EqWMA
* EWMA 
* GARCH(1,1) 

 <img width="727" alt="image" src="https://user-images.githubusercontent.com/62723280/175792706-b34297ae-dd08-46fa-bc9c-ff67e7dd23f0.png">


The models were also tested visually using QQ-plots and ECDFS. Other stylized facts were also examined for the return distributions.

### Dependency Modelling
 
When modelling multiple financial assets the dependency between the assets must be considered. In order to do this a multivariate distribution is required. This is done by using copulas in conjunction with the univariate distributions found in the eariler volatility modelling part. 

<img width="1097" alt="image" src="https://user-images.githubusercontent.com/62723280/175792653-dd53aadb-4b6e-45e1-9d8a-1c1a9cde7875.png">

Using copulas we are able to simulate future returns, and thus prices, of financial assets with a correct dependency strucutre. In this part we look at **NOK/USD** and **EUR/USD**.

### Risk-Assessment-and-Backtesting
Risk Modelling with Value at Risk using different approaches, such as historical simulation, Extreme Value Theory and risk-factor mapping. Based on labs in Financial Risk Management at Liu.
