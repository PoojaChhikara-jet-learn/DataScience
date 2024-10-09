import pandas as pd

# Load the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_data = pd.read_csv(url, header=None, names=columns)

# Display the dataset head and info
print("Dataset Head:")
print(iris_data.head())

print("\nDataset Info:")
print(iris_data.info())

# Calculate mean, min, and max
print("\nStatistics:")
print("Mean Petal Length:", iris_data["petal_length"].mean())
print("Min Petal Length:", iris_data["petal_length"].min())
print("Max Petal Length:", iris_data["petal_length"].max())

print("Mean Petal Width:", iris_data["petal_width"].mean())
print("Min Petal Width:", iris_data["petal_width"].min())
print("Max Petal Width:", iris_data["petal_width"].max())

print("Mean Sepal Length:", iris_data["sepal_length"].mean())
print("Min Sepal Length:", iris_data["sepal_length"].min())
print("Max Sepal Length:", iris_data["sepal_length"].max())

print("Mean Sepal Width:", iris_data["sepal_width"].mean())
print("Min Sepal Width:", iris_data["sepal_width"].min())
print("Max Sepal Width:", iris_data["sepal_width"].max())

# Count rows for each species
print("\nCount of Rows for Each Species:")
print(iris_data["species"].value_counts())
