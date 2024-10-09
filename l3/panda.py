import pandas as pd

# Create a dictionary of data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 30, 22, 35,32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston','San Francisco'],
    'Pclass': [1, 2, 2, 3, 1],
    'Sex': ['female', 'male', 'male', 'male', 'female'],
    'Fare': [100, 20, 30, 15, 150]
}

# Create a DataFrame from the dictionary
dataset = pd.DataFrame(data)
print("headers",dataset.head())
print(dataset.info())

print(dataset.describe())


# Display the dataset
print("dataset is:",dataset)



# Select rows where Age is greater than 25
filtered_rows = dataset[dataset['Age'] > 25]

# Select specific columns
selected_columns = dataset[['Name', 'City']]

print("Filtered Rows:\n", filtered_rows)
print("\nSelected Columns:\n", selected_columns)

# combine multiple conditions
# Filtering for classes 2 and 3 using isin()
class2And3 = dataset[dataset["Pclass"].isin([2, 3])]
print("Class 2 and 3 passengers:")
print(class2And3[["Name", "Pclass"]].head())
print("Shape:", class2And3.shape)

# Combining conditions with OR (|)
class2And3 = dataset[(dataset["Pclass"] == 2) | (dataset["Pclass"] == 3)]
print("\nClass 2 or 3 passengers:")
print(class2And3[["Name", "Pclass"]].head())
print("Shape:", class2And3.shape)

# Combining conditions with AND (&) to get mean fare of male first class passengers
maleFirstClass = dataset[(dataset["Sex"] == "male") & (dataset["Pclass"] == 1)]
print("\nMean fare of male first class passengers:", maleFirstClass["Fare"].mean())
