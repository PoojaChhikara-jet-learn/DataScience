import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
income_data = pd.read_csv('datasets/adult.csv', header=None, names=[
    'age', 'workclass', 'fnlwgt', 'education', 'education_num',
    'marital_status', 'occupation', 'relationship', 'race', 'gender',
    'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income'
])

# Display the first few rows
print("First few rows of the dataset:")
print(income_data.head())

# Data Information and Summary Statistics
print("\nData Information:")
income_data.info()

print("\nSummary Statistics:")
print(income_data.describe())

# Replace '?' with NaN and count missing values
income_data.replace(' ?', np.nan, inplace=True)
print("\nMissing values per column:")
print(income_data.isnull().sum())

# Drop rows with missing values
income_data.dropna(inplace=True)
print("\nData shape after removing missing values:", income_data.shape)

# Drop irrelevant columns (based on assumed analysis requirements)
income_data.drop(['fnlwgt', 'education_num'], axis=1, inplace=True)

# Encode categorical variables
# Income: <=50K -> 0, >50K -> 1
income_data['income'] = income_data['income'].map({' <=50K': 0, ' >50K': 1})

# Gender: Male -> 0, Female -> 1
income_data['gender'] = income_data['gender'].map({' Male': 0, ' Female': 1})

# Race: Convert categories to numeric labels
income_data['race'] = income_data['race'].astype('category').cat.codes

# Marital Status: Convert categories to numeric labels
income_data['marital_status'] = income_data['marital_status'].astype('category').cat.codes

# Relationship: Convert categories to numeric labels
income_data['relationship'] = income_data['relationship'].astype('category').cat.codes

# Workclass: Convert categories to numeric labels
income_data['workclass'] = income_data['workclass'].astype('category').cat.codes

# Occupation: Convert categories to numeric labels
income_data['occupation'] = income_data['occupation'].astype('category').cat.codes

# Native Country: Convert categories to numeric labels
income_data['native_country'] = income_data['native_country'].astype('category').cat.codes

# Check the cleaned and encoded data
print("\nCleaned and encoded data:")
print(income_data.head())

# Data Visualizations
# Income distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='income', data=income_data, palette='viridis')
plt.title('Income Distribution')
plt.xlabel('Income')
plt.ylabel('Count')
plt.xticks(ticks=[0, 1], labels=['<=50K', '>50K'])
plt.show()

# Age Distribution
plt.figure(figsize=(10, 6))
sns.histplot(income_data['age'], kde=True, bins=30, color='blue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Density')
plt.show()

# Education vs Income
plt.figure(figsize=(12, 6))
sns.barplot(x='education', y='income', data=income_data, palette='plasma', ci=None)
plt.xticks(rotation=90)
plt.title('Average Income by Education Level')
plt.xlabel('Education Level')
plt.ylabel('Proportion with Income >50K')
plt.show()

# Gender vs Income
plt.figure(figsize=(8, 5))
sns.barplot(x='gender', y='income', data=income_data, palette='coolwarm', ci=None)
plt.title('Income by Gender')
plt.xlabel('Gender')
plt.ylabel('Proportion with Income >50K')
plt.xticks(ticks=[0, 1], labels=['Male', 'Female'])
plt.show()

# Workclass vs Income
plt.figure(figsize=(12, 6))
sns.barplot(x='workclass', y='income', data=income_data, palette='mako', ci=None)
plt.title('Income by Workclass')
plt.xlabel('Workclass')
plt.ylabel('Proportion with Income >50K')
plt.xticks(rotation=90)
plt.show()

# Race vs Income
plt.figure(figsize=(10, 5))
sns.barplot(x='race', y='income', data=income_data, palette='cubehelix', ci=None)
plt.title('Income by Race')
plt.xlabel('Race')
plt.ylabel('Proportion with Income >50K')
plt.show()

# Marital Status vs Income
plt.figure(figsize=(12, 6))
sns.barplot(x='marital_status', y='income', data=income_data, palette='autumn', ci=None)
plt.title('Income by Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Proportion with Income >50K')
plt.xticks(rotation=90)
plt.show()

# Relationship vs Income
plt.figure(figsize=(10, 5))
sns.barplot(x='relationship', y='income', data=income_data, palette='spring', ci=None)
plt.title('Income by Relationship Status')
plt.xlabel('Relationship Status')
plt.ylabel('Proportion with Income >50K')
plt.xticks(rotation=90)
plt.show()

# Capital Gain vs Income
plt.figure(figsize=(8, 5))
sns.boxplot(x='income', y='capital_gain', data=income_data, palette='Set3')
plt.title('Capital Gain Distribution by Income')
plt.xlabel('Income')
plt.ylabel('Capital Gain')
plt.xticks(ticks=[0, 1], labels=['<=50K', '>50K'])
plt.show()

# Capital Loss vs Income
plt.figure(figsize=(8, 5))
sns.boxplot(x='income', y='capital_loss', data=income_data, palette='Set2')
plt.title('Capital Loss Distribution by Income')
plt.xlabel('Income')
plt.ylabel('Capital Loss')
plt.xticks(ticks=[0, 1], labels=['<=50K', '>50K'])
plt.show()
