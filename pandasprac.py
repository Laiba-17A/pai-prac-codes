import pandas as pd
import numpy as np

# ===================================================
# 1️⃣ Create a Sample Titanic-like Dataset
# ===================================================
data = {
    'PassengerId': range(1, 11),
    'Survived': [1, 0, 1, 1, 0, 0, 1, 0, 1, 1],
    'Sex': ['female', 'male', 'female', 'female', 'male', 'male', 'female', 'male', 'female', 'female'],
    'Age': [22, 35, 26, np.nan, 40, 28, 19, 50, np.nan, 30],
    'Fare': [7.25, 71.28, 7.92, 53.10, 8.05, 8.46, 12.50, 7.89, 30.00, 23.45],
    'Embarked': ['S', 'C', 'S', 'S', 'S', 'Q', 'Q', 'S', 'C', 'S']
}

df = pd.DataFrame(data)
print("=== Original Dataset ===")
print(df)

# ===================================================
# 2️⃣ Basic Data Exploration
# ===================================================
print("\n=== Basic Info ===")
print(df.info())

print("\n=== Statistical Summary ===")
print(df.describe())

print("\n=== Columns ===")
print(df.columns)

print("\n=== Shape (Rows, Columns) ===")
print(df.shape)

print("\n=== First 5 Rows ===")
print(df.head())

print("\n=== Missing Values ===")
print(df.isnull().sum())

# Fill missing ages with mean age
df['Age'].fillna(df['Age'].mean(), inplace=True)

# ===================================================
# 3️⃣ Data Manipulation
# ===================================================
# Convert 'Sex' to numeric (male=0, female=1)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Add a new column 'AgeGroup' based on condition
df['AgeGroup'] = np.where(df['Age'] >= 30, 'Senior', 'Young')

# Sort by Fare (descending)
df.sort_values(by='Fare', ascending=False, inplace=True)

# Create a filtered dataset for survivors
survived_df = df[df['Survived'] == 1]

print("\n=== After Manipulation ===")
print(df)

# ===================================================
# 4️⃣ Solve 5 Common Analysis Problems
# ===================================================

# 1️⃣ Average Fare by Gender
avg_fare_by_sex = df.groupby('Sex')['Fare'].mean()
print("\n1️⃣ Average Fare by Gender:")
print(avg_fare_by_sex)

# 2️⃣ Overall Survival Rate
survival_rate = (df['Survived'].sum() / len(df)) * 100
print("\n2️⃣ Overall Survival Rate: {:.2f}%".format(survival_rate))

# 3️⃣ Passengers by Embarked Port
embark_counts = df['Embarked'].value_counts()
print("\n3️⃣ Passengers by Embarked Port:")
print(embark_counts)

# 4️⃣ Average Age of Survivors vs Non-Survivors
avg_age = df.groupby('Survived')['Age'].mean()
print("\n4️⃣ Average Age (Survived vs Non-Survived):")
print(avg_age)

# 5️⃣ Correlation Between Age, Fare, and Survival
correlation = df[['Age', 'Fare', 'Survived']].corr()
print("\n5️⃣ Correlation Matrix:")
print(correlation)

# ===================================================
# 5️⃣ Final Clean Data
# ===================================================
print("\n=== Final Cleaned Dataset ===")
print(df)

# Optional: save to Excel if needed
# df.to_excel("clean_titanic_dataset.xlsx", index=False)
