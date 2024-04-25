%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
mtcars = pd.read_csv("/content/mtcars.csv")
mtcars = mtcars.rename(columns={'Unnamed: 0': 'model'})
mtcars.index = mtcars.model
del mtcars['model']

mtcars.head()

#measure of central_tendency
mtcars.mean()

mtcars.median()

mtcars.mode()

#measue of spread-dispersion
#range of mpg
max(mtcars["mpg"]) - min(mtcars["mpg"])

five_num = [mtcars["mpg"].quantile(0),
mtcars["mpg"].quantile(0.25),
mtcars["mpg"].quantile(0.50),
mtcars["mpg"].quantile(0.75),
mtcars["mpg"].quantile(1)]
five_num

mtcars["mpg"].describe()

#Interqurtile Range
mtcars["mpg"].quantile(0.75) - mtcars["mpg"].quantile(0.25)
mtcars.boxplot(column="mpg",
return_type="axes",
figsize=(8,8))

plt.text(x=0.74, y=22.25, s="3rd Quartile")
plt.text(x=0.8, y=18.75, s="Median")
plt.text(x=0.75, y=15.5, s="1st Quartile")
plt.text(x=0.9, y=10, s="Min")
plt.text(x=0.9, y=33.5, s="Max")
plt.text(x=0.7, y=19.5, s="IQR", rotation=90, size=25);

#Variance
mtcars["mpg"].var()

#standar_deviation
mtcars["mpg"].std()

from numpy import absolute
A = 20
sum = 0

#absolute deviation calculation
for i in range(len(mtcars)):
  av = absolute(mtcars["mpg"][i] - A)

# Absolute value of the differences of each data point and A
# Summing all those absolute values
sum = sum + av

# finding the absolute deviation
print(sum / len(mtcars))

# Compute percentiles using NumPy
percentiles = np.percentile(mtcars["mpg"], [10, 25, 50, 75, 90])
print("10th, 25th, 50th, 75th, and 90th percentiles of mpg:")
print(percentiles)
