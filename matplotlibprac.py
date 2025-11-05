import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===================================================
# 1️⃣ Create a Titanic-like Dataset
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

# Handle missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Convert Sex to numeric for easier analysis
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

print("=== Titanic-like Data ===")
print(df)

# ===================================================
# 2️⃣ Bar Chart → Number of Passengers by Embarked Port
# ===================================================
embark_counts = df['Embarked'].value_counts()

plt.figure(figsize=(6,4))
plt.bar(embark_counts.index, embark_counts.values, color='skyblue')
plt.title('Number of Passengers by Embarked Port')
plt.xlabel('Port of Embarkation')
plt.ylabel('Number of Passengers')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()

# ===================================================
# 3️⃣ Histogram → Age Distribution
# ===================================================
plt.figure(figsize=(6,4))
plt.hist(df['Age'], bins=5, color='lightgreen', edgecolor='black')
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Number of Passengers')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()

# ===================================================
# 4️⃣ Line Graph → Fare vs PassengerId
# ===================================================
plt.figure(figsize=(6,4))
plt.plot(df['PassengerId'], df['Fare'], marker='o', color='purple')
plt.title('Fare by Passenger ID')
plt.xlabel('Passenger ID')
plt.ylabel('Fare')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# ===================================================
# 5️⃣ Extra Example → Compare Average Fare by Gender (Bar)
# ===================================================
avg_fare_by_gender = df.groupby('Sex')['Fare'].mean()

plt.figure(figsize=(5,4))
plt.bar(['Male', 'Female'], avg_fare_by_gender.values, color=['orange', 'pink'])
plt.title('Average Fare by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Fare')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
