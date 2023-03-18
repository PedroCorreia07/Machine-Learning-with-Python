import matplotlib.pyplot as plt

import pandas as pd
import pylab as pl
import numpy as np


df=pd.read_csv(r'C:\Users\pedro\source\repos\PedroCorreia07\Machine-Learning-with-Python\Simple Linear Regression Project\FuelConsumptionCo2.csv')
print(df.head())
print(df.describe())
cdf=df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB_MPG','CO2EMISSIONS']]
print(cdf.head(9))
print(cdf.hist())
print(plt.show())