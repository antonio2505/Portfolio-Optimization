#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 19:10:05 2022

@author: kassi
"""

import pandas_datareader as pdr
#from pandas_datareader import data, wp
from datetime import date
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

risk_free_rate = 0.05

def capm(start_data, end_date, ticker1, ticker2):
    #get the data from yahoo finance
    stock1 = pdr.get_data_yahoo(ticker1, start_data, end_date)
    stock2 = pdr.get_data_yahoo(ticker2, start_data, end_date)
    
    #we prefer monthly return instead of daily return
    return_stock1 = stock1.resample("M").last()
    return_stock2 = stock2.resample("M").last()
    
    #Creating a dataframe from the data - Adj close
    data = pd.DataFrame({"s_adjclose":return_stock1['Adj Close'], "m_adjclose":return_stock2['Adj Close']}, index=return_stock1.index)
    #natural logarithm of the return
    data[['s_return','m_return']] = np.log(data[["s_adjclose","m_adjclose"]]/data[["s_adjclose","m_adjclose"]].shift(1))
    #no need for missing value NaN
    data= data.dropna()
    
    #Covariance Metrix: the diagonal are the variance: the off diagonal are the covariance
    #the matrix symetric is: cov[1,0] = cov[0,1]
    covmat = np.cov(data['s_return'], data['m_return'])
    
    #calculating the beta according to the formular
    beta = covmat[1,0]/covmat[1,1]
    print("Beta From Formular: ", beta)
    
    #using the linear Regression
    beta,alpha = np.polyfit(data["m_return"],data['s_return'], deg=1)
    print("Beta From Regression: ", beta)
    print("Alpha: ",alpha)
    
    #plot
    fig, axis = plt.subplots(1, figsize=(20, 10))
    axis.scatter(data['m_return'],data['s_return'],label='Data points')
    axis.plot(data['m_return'],beta*data['m_return']+alpha,color='red',label='CAPM Line')
    plt.title("Capital Asset Pricing Model, finding the Alpha and the Beta")
    plt.xlabel("Market Return $R_m$", fontsize=18)
    plt.ylabel("Stock Return $R_a$", fontsize=18)
    plt.text(0.08,0.05,r'$R_a = \beta * R_m + \alpha$',fontsize=18)
    plt.legend()
    plt.grid()
    plt.show()
    
    #Calculating the expected return according to the CAPM
    expected_return =risk_free_rate + beta*(data['m_return'].mean()*12-risk_free_rate)
    print("Expected Return: ",expected_return)
    
if __name__=="__main__":
    
    #using historical data from 2010 to 2017: the marker is the sp500
    capm("2010-01-01","2022-01-01",'AMZN',"^GSPC")
    
    
    
    
    
    
    
    
    
    
    
    
    