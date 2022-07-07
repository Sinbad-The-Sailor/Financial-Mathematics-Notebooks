# Financial Mathematics Notebooks
Notebooks containing examples and labs of matematical finance. 

### Volatility Modelling

Three different volatility models are examined for the return processes of financial assets. The models examined are given below with a corresponding volatility plot over time.

* EqWMA
* EWMA 
* GARCH(1,1) 

An example of a GARCH(1,1) volatility estimation for the S&P 500 index. 

<p align="center">
 <img width="727" alt="image" src="https://user-images.githubusercontent.com/62723280/175792706-b34297ae-dd08-46fa-bc9c-ff67e7dd23f0.png">
</p>

The models were also tested visually using QQ-plots and ECDFS. Other stylized facts were also examined for the return distributions.

### Dependency Modelling
 
While modelling multiple financial assets the dependency between the assets must be considered. In order to do this a multivariate distribution is required. This is done by using copulas in conjunction with the univariate distributions. In this notebook multiple copulas are used to fit **NOK/USD** and **EUR/USD** returns. 


<p align="center">
<img width="1097" alt="image" src="https://user-images.githubusercontent.com/62723280/175792653-dd53aadb-4b6e-45e1-9d8a-1c1a9cde7875.png">
</p>

Above are the copula densities and their contours.

### Risk Measurements and Backtesting
TODO: Complete.

### Extreme Value Theory

To obtain a better estimate of Value at Risk and Expected Shortfall for high confidence levels EVT can be employed. EVT estimates a parametric distribution for losses above some threshold (POT approach to EVT). This threshold is set to the 95th percentile of the loss distribution, i.e., losses above VaR 95. EVT have better estimates since it matches the tail events of the sample better than a single normal distribution, or even fat tailed distributions.

<p align="center">
<img width="423" alt="image" src="https://user-images.githubusercontent.com/62723280/177868942-1ead6f46-e1cb-45f8-acfc-013c9f8474b0.png">
</p>

Using EVT a emprical loss distribution of S&P500 from 2007 to 2017 a parametric loss distribution is ascertained, after which VaR and ES are calculated. The VaR and ES becomes 11.5% and 13.6% respectivley. Contrasted with vanilla empirical VaR and ES which were 17.1% and 20.1% respectively. Clearly overestimating the risk.

### Risk Factor Mapping
TODO: Complete.

### Fund Performace
The 'Washington Mutual Investors Fund' (CWMAX) fund was be examined by its performance. Different performance metrics was be used to judge the fund returns. Multifactor methods was also employed to obtain a greater understanding of its performance. 

<p align="center">
<img width="1063" alt="image" src="https://user-images.githubusercontent.com/62723280/176040565-1e5ef98a-310a-45e2-9d41-93bb2c7bfdc7.png">
</p>

### Fund FX-Hedging
TODO: Complete.

### Options Portfolio Strategy
TODO: Complete.

### Mean Variance Model
TODO: Complete.

### Markov Chain Credit Ratings Process
TODO: Add.

### Interest Rate Curve Building and Interpolation
TODO: Add.
