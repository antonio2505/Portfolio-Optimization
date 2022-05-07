'''
MODERN PORTFOLIO THEORY

it was formulated in the 1950 by Harry Markowitz.

what is the main idea?
A single stock is quite unpredictable or risky: we do not know for certain
whether a stock will go up or down.
##single_stock_plot

But we may combine several stocks, in order to reduce risk as much as possible.
"DIVERSIFICATION."
when a given value of stock goes down another goes up.
Combining assets in the main idea: it is the same as the black-schoes Model.
##combining_mult_asset_plot

The model has some Assumptions:
    * the return are normally distributed:
        with mean (u) and variance(sigma)
    * the investors are risk-averse:
        inverstor will take more risk if the are excepting more rewards
low --> low return
higher risk --> higher return

with modern portfolio theory, investors can construct optimal portfolios
offering the maximum possible expected return for a given level of risk!!!

so what is an efficient portfolio?
it is a portfolio that has the highest rewards for a given level of risk.

** How to calculate the return of an asset ?
## return_asset
##daily_return_plot
Wi is the weight of the i stock.
ri the return of the i stock // calculate on its historical data
Ui the expected return of the portfolio
## port_return_formula

this model relies on historical data. Historical Data mean performance is assumed
to be the best estimator for future performance.

** what about the risk of the portfolio ?
    the risk has something to do with volatility
    volatility has something to do with the standard deviation

covariance meaure how much 2 point(or stocks ij) vary together
## covariance formula
## covariance_form ..> negative covariance means returns move inversely
                    ..> positie covariance means returns move together

Markowitz's theory is about diversification: possessing assets(stocks)
    with high positive covariance does not provide very much
    diversification!!!
    * the aim of diversification is to eliminate fluctuations in the
    long term.. so uncorrelated stocks are better!!
 ##variance_formula
for calculating the variance of the portfolio we need the covariance matrix
cointaining all the covariances of the stocks involved in the portfolio.
## variance_portfo

** Efficient Frontier

every dots in the plot represent w (weight) --> so different portfolios or
                                                set of portolio
An investor is interested in :
    1.) the maximum return given a fixed risk level
    2.) minimum risk given a fixed return

these portfolio make up the so called efficient-frontier!!!
this is the main feature of Markowitz model: the investor can decide the
risk or the expected return

--> basic rule: if you want to make money, you have to take risk!!!

** What is Shape Ratio ?

it is one of the most important risk/return measures used in finance
--> it describes how much excess return you are receiving for
    extra volatility that you endure holding a riskier asset(stock)
    a sharpe-ratio S(x)>1 is considered to be good.
 ## sharpe-ratio formula

** Capital allocation line:

  The optimal portfolio lie on the capital allocation line if the
  portfolio can containe stocks as well as risk-free rate(bond)
if you dont want to take risk you will be on the risk-free point that contain
zero risk.

** IMPLEMENTATION IN PYTHON

--Weights:



























'''
