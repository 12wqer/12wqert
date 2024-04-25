# -*- coding: utf-8 -*-
"""visualize_num_cat.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IQdXUrs4mxlKuz5FNmKU_UQDpAgYx6pa
"""

# Importing necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading the Titanic dataset
titanic_df = sns.load_dataset("titanic")

# Exploratory Data Analysis (EDA)

## Quantitative Data Visualization
# Histograms for numerical variables
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
sns.histplot(titanic_df['age'].dropna(), kde=True, color='skyblue')
plt.title('Distribution of Age')

plt.subplot(2, 2, 2)
sns.histplot(titanic_df['fare'], kde=True, color='salmon')
plt.title('Distribution of Fare')

plt.subplot(2, 2, 3)
sns.histplot(titanic_df['parch'], kde=True, color='green')
plt.title('Distribution of Parents/Children Aboard')

plt.subplot(2, 2, 4)
sns.histplot(titanic_df['sibsp'], kde=True, color='orange')
plt.title('Distribution of Siblings/Spouses Aboard')

plt.tight_layout()
plt.show()

# Bar plot for categorical variable (Survived)
plt.figure(figsize=(8, 5))
sns.countplot(data=titanic_df, x='survived', hue='survived', palette='Set2', legend=False)
plt.title('Survival Counts')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.xticks(ticks=[0, 1], labels=['No', 'Yes'])
plt.show()

## Qualitative Data Visualization (Non-numeric)
# Pairplot for pairwise relationships between numerical variables
sns.pairplot(titanic_df[['survived', 'age', 'fare', 'parch', 'sibsp']], hue='survived', palette='husl', diag_kind='auto')
plt.suptitle('Pairwise Relationships between Numerical Variables', y=1.02)
plt.show()