# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lQOhYLy3PPYUGgvpBUaJ_j218szD9aSq

**THE SPARKS FOUNDATION - GRADUATE ROTAIONAL INTERNSHIP PROGRAM**

**DATA SCIENCE AND BUSINESS ANALYTICS TASKS**

Task 1- Supervised Learning by Linear Regression in Python.

Supervised machine learning algorithms are designed to learn by example. When training a supervised learning algorithm, the training data will consist of inputs paired with the correct outputs. During training, the algorithm will search for patterns in the data that correlate with the desired outputs. After training, a supervised learning algorithm will take in new unseen inputs and will determine which label the new inputs will be classified as based on prior training data. The objective of a supervised learning model is to predict the correct label for newly presented input data. A supervised learning algorithm can be written simply as: Y=f(x).
Where Y is the predicted output that is determined by a mapping function that assigns a class to an input value x. The function used to connect input features to a predicted output is created by the machine learning model during training.

Simple linear regression is useful for finding relationship between two continuous variables. One is predictor or independent variable and other is response or dependent variable. It looks for statistical relationship but not deterministic relationship. Relationship between two variables is said to be deterministic if one variable can be accurately expressed by the other. The core idea is to obtain a line that best fits the data. The best fit line is the one for which total prediction error (all data points) are as small as possible. Error is the distance between the point to the regression line.

The given code shows prediction of students' percentage score based on his/her hours of study. The following model is trained with 75% of data using Linear Regression and is tested using the remaining 25% of data.


*   Name:   Riva Desai
*   github: https://github.com/Riva13/TSF-GRIP-Task-1
*   LinkedIn: https://www.linkedin.com/in/riva-desai-620354166/

Importing pandas, numpy and pyplot libraries.
"""

import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

"""Importing data from given data source i.e. http://bit.ly/w-data consisting of two columns Hours and Score for hours of study and percentage score respectively."""

url = "http://bit.ly/w-data"
s_data = pd.read_csv(url)
print("Data imported")

s_data.head(5)

"""Plotting the imported data on a graph."""

s_data.plot(x='Hours', y='Scores', style='o')  
plt.title('Hours vs Score')  
plt.xlabel('Hours of Study')  
plt.ylabel('Percentage Score')  
plt.show()

"""Extracting two variable arrays X and y i.e. hours of study and percentage score respectively.  """

X = s_data.iloc[:, :-1].values  
y = s_data.iloc[:, 1].values

"""Splitting the data into Training and Testing sets. Here testing size is 0.25 which means that 25% is testing data and 75% is training data."""

from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                            test_size=0.25, random_state=0)

"""ScikitLearn i.e. sklearn library is extremely efficient library and has numerous built-in functions for various algorithms, Linear Regression being one of them. It is simply needed to fit the variales in regressor from LinearRegression libarary."""

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(X_train, y_train)

"""Plotting the regression line on graph."""

line = regressor.coef_*X
plt.scatter(X, y)
plt.plot(X, line, color='red')

"""Using predict function of regressor to predict the percentage score of the students in the testing data and comparing the output with actual data."""

y_pred = regressor.predict(X_test)

X_test.reshape(1,-1)
df = pd.DataFrame({'Hours of Study': X_test[:,0], 'Actual': y_test, 'Predicted': y_pred})
print(df)

"""Testing the model with unknown value."""

hour=input('Enter hours: ')
hours = float(hour)
hr=np.array([hours])
hr=hr.reshape(-1,1)
own_pred = regressor.predict(hr)
print("No of Hours = {}".format(hours))
print("Predicted Score = {}".format(own_pred[0]))

"""Evaluating the model using Mean Absolute Error(MAE). MAE is the mean of all the absolute error that is the absolute difference between true value and the predicted value for given observation."""

from sklearn import metrics  
print('Mean Absolute Error:', 
      metrics.mean_absolute_error(y_test, y_pred))