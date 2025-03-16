import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
# Splitting the data into training and testing
from sklearn.model_selection import train_test_split
# Algorithm that we would be using
from sklearn.tree import DecisionTreeClassifier
# for finding accuracy
from sklearn import metrics

# Load the Titanic dataset
data = pd.read_csv('datasets/titanic.csv')

# Verify that the data has been successfully imported
print(data.head())
print(data.info())

# Data Preprocessing
# Select relevant columns and handle missing values
data = data[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
# data['Age'].fillna(data['Age'].median(), inplace=True)  # Fill missing Age with median
# data['Fare'].fillna(data['Fare'].median(), inplace=True)  # Fill missing Fare with median

imputer = SimpleImputer(strategy='median')
data[['Age', 'Fare']] = imputer.fit_transform(data[['Age', 'Fare']])

# Impute missing values for Sex with the most frequent value
imputer_sex = SimpleImputer(strategy='most_frequent')
data['Sex'] = imputer_sex.fit_transform(data[['Sex']])

# Convert categorical variables to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# Check for any remaining missing values
print(data.isnull().sum())

# Define features (X) and target (Y)
Y = data['Survived']
X = data.drop('Survived', axis=1)

# Splitting the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Initialize and train the Decision Tree Classifier
model = DecisionTreeClassifier(max_depth=3, random_state=1)
model.fit(X_train, Y_train)

# Make predictions on the testing set
predictions = model.predict(X_test)

# Calculate and print the accuracy
accuracy = metrics.accuracy_score(Y_test, predictions)
print("Accuracy:", accuracy)

# Optional: Visualize the Decision Tree
from sklearn.tree import plot_tree

plt.figure(figsize=(10, 6))
plot_tree(model, feature_names=X.columns, class_names=['Not Survived', 'Survived'], filled=True)
plt.title("Decision Tree Visualization")
plt.show()
