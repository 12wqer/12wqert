# -*- coding: utf-8 -*-
"""bowley skew.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19IBxPCkSTybzf9fqVG50r23W_BcoOsaN
"""

import numpy as np

def bowley_skewness_coefficient(x):
    # Calculate median and quartiles
    q1 = np.percentile(x, 25)
    q2 = np.percentile(x, 50)
    q3 = np.percentile(x, 75)

    # Calculate Bowley's coefficient of skewness
    sk = (q1 + q3 - 2 * q2) / (q3 - q1)
    return sk

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 50])  # Example array
#example array x = np.array([1, 2, 3, 4, 6, 8, 10, 12, 14, 16])
sk = bowley_skewness_coefficient(x)
print("Bowley's coefficient of skewness:", sk)