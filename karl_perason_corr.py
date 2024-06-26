# -*- coding: utf-8 -*-
"""karl_perason_corr.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AlbIDQ_i7sGraL956wEEGbNOFeeiSHMz
"""

import numpy as np

def pearson_correlation_coefficient(x, y):
    # Calculate mean and standard deviation
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_std = np.std(x)
    y_std = np.std(y)

    # Calculate Covariance
    covariance = np.sum((x - x_mean) * (y - y_mean)) / len(x)

    # Calculate Pearson's correlation coefficient
    r = covariance / (x_std * y_std)
    return r

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

r = pearson_correlation_coefficient(x, y)
print("Pearson's correlation coefficient:", r)