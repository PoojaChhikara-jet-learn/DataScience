import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Splitting the data into training and testing
from sklearn.model_selection import train_test_split
# Algorithm that we would be using
from sklearn.tree import DecisionTreeClassifier
# for finding accuracy
from sklearn import metrics

# get the data into the program
data = pd.read_csv('DS/l7/iris.csv')

# verify that the data has been successfully imported
print(data.head())
print(data.info())

# data preprocessing
# setosa - 0,  versicolor - 1, virginica - 2,
data["species"] = data["species"].replace({"setosa":0, "versicolor":1, "virginica":2})

# Basic data-analysis step, could be left in the interest of time since we are not dropping any columns over here
"""
# graph of petal_height vs speices, petal_width vs species, sepal_length vs speciesm sepal_width vs species
plt.subplot(221)
plt.scatter(data["petal_length"], data["species"], s = 10, c = 'green', marker = 'o')
plt.subplot(222)
plt.scatter(data["petal_width"], data["species"], s = 10, c = 'red', marker = 'o')
plt.subplot(223)
plt.scatter(data["sepal_length"], data["species"], s = 10, c = 'blue', marker = 'o')
plt.subplot(224)
plt.scatter(data["sepal_width"], data["species"], s = 10, c = 'orange', marker = 'o')
plt.show()
"""

Y = data["species"]

X = data.drop("species", axis = 1)
#print(X.head())
print(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1)

print(X_train.shape)
print(X_test.shape)

model = DecisionTreeClassifier(max_depth = 3, random_state = 1)

model.fit(X_train, Y_train)

predictions = model.predict(X_test)

print("Accuracy ", metrics.accuracy_score(predictions, Y_test))