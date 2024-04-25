# -*- coding: utf-8 -*-
"""data visualization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O-211yEH0I_kDBTH5H67fyqPSKnxUQvc
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import Series, DataFrame
import plotly.express as px

df1=pd.read_csv('/content/tips.csv')

print(df1)

#Univariate
#Box Plot

df1['total_bill'].describe()

fig = px.box(df1, y='total_bill')
fig.show()

fig = px.histogram(df1, x='total_bill')
fig.show()

#Multivariate
#Heatmap and Scatterplot

#Scatter plot
fig1 = px.scatter(df1, x='total_bill', y='tip', color='time')
fig1.show()

#Heatmap
hd = []
ld = []
dd = []
tld = []
tdd = []
fld = []
fdd = []
sald = []
sadd = []
suld = []
sudd = []

for i in range(244):
    if df1["time"][i] == 'Lunch':
        if df1["day"][i] == 'Thur':
            tld.append(df1["size"][i])
        elif df1["day"][i] == 'Fri':
            fld.append(df1["size"][i])
        elif df1["day"][i] == 'Sat':
            sald.append(df1["size"][i])
        else:
            suld.append(df1["size"][i])
    else:
        if df1["day"][i] == 'Thur':
            tdd.append(df1["size"][i])
        elif df1["day"][i] == 'Fri':
            fdd.append(df1["size"][i])
        elif df1["day"][i] == 'Sat':
            sadd.append(df1["size"][i])
        else:
            sudd.append(df1["size"][i])

ld.append(sum(tld))
ld.append(sum(fld))
ld.append(sum(sald))
ld.append(sum(suld))
dd.append(sum(tdd))
dd.append(sum(fdd))
dd.append(sum(sadd))
dd.append(sum(sudd))

hd.append(ld)
hd.append(dd)

fig = px.imshow(hd,
                labels=dict(x="day", y="time", color="size"),
                x=['Thur', 'Fri', 'Sat', 'Sun'],
                y=['Lunch', 'Dinner']
                )

fig.update_xaxes(side="top")
fig.show()

#Bubble Chart
import plotly.express as px

fig = px.scatter(df1, x="size", y="total_bill", color="day", size='tip', hover_data=['sex'])
fig.show()

#Density plot
import matplotlib.pyplot as plt

# Density plot for 'tip'
df1['tip'].plot.density(color='green')
plt.title('Density Plot for Tip')
plt.show()

#less than ogive
import numpy as np
import matplotlib.pyplot as plt

data = df1["tip"]
print(max(data))
print(min(data))

# Creating class interval
classInterval = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculating frequency and class interval
values, base = np.histogram(data, bins=classInterval)

# Calculating cumulative sum
cumsum = np.cumsum(values)

# Plotting the ogive graph
plt.plot(base[1:], cumsum, color='red', marker='o', linestyle='-')

# Formatting
plt.title('Ogive Graph')
plt.xlabel('Tip')
plt.ylabel('Cumulative Frequency')

plt.show()

#more than ogive
# Reversing cumulative frequency
res = np.flipud(cumsum)

# Plotting ogive
plt.plot(base[1:], res, color='brown', marker='o', linestyle='-')

# Formatting the graph
plt.title('Ogive Graph')
plt.xlabel('Tip')
plt.ylabel('Cumulative Frequency')

plt.show()

#Pie chart
cd = [sum(ld), sum(dd)]
time = ['Lunch', 'Dinner']

plt.pie(cd, labels=time)
plt.title("Number of customers during Lunch and Dinner")
plt.show()

#Line chart / Run_chart
import plotly.express as px

fig = px.line(df1, x=range(244), y="tip", title='Tips per customer')
fig.show()

