# -*- coding: utf-8 -*-
"""Skweness and Kurtosis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KQzokSE_MeUNUkJcOSRugJXXKv5M98dP
"""

from scipy.stats import skew, kurtosis
def calculate_skewness(x):
  sk=skew(x)
  return sk

def calculate_kurtosis(x):
  kurt=kurtosis(x)
  return kurt

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics

#Plot between -10 to 10 with .001 steps
x=np.array([1,2,3,4,5,6,7,8,9,10])

#Calculating mean and Standard Deviation
mean = statistics.mean(x)
sd=statistics.stdev(x)

plt.plot(x, norm.pdf(x,mean,sd))
plt.show()

sk=calculate_skewness(x)
kurt=calculate_kurtosis(x)

print("Skewness:", sk)
print("Kurtosis:", kurt)