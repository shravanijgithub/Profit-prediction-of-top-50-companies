# -*- coding: utf-8 -*-
"""Exposys Data Lab

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y_2SBdNZRXrvqBjaxzn2glg_kDSZHqjB
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import missingno as msno
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# %matplotlib inline

df=pd.read_csv("/content/50Startups.csv")

df.head()

df.info()

df.describe()

df.dropna()

df.columns

sns.pairplot(df)

X=df[['R&D Spend','Administration','Marketing Spend']]

X.shape

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X = ss.fit_transform(X)

y = df['Profit']

y.shape

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression

lr = LinearRegression ()

lr.fit(X_train,y_train)

y_pred = lr.predict (X_test)

y_pred

from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
from sklearn.model_selection import train_test_split

mean_absolute_error(y_test,y_pred)

mean_absolute_percentage_error(y_test,y_pred)

lr.score(X_test,y_test)

