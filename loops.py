
# ============================================================
# 🧠 Python Loops + "in" / "not in" + Pandas Filtering
# ============================================================

import pandas as pd

print("========== BASIC PYTHON LOOPS ==========\n")

# ============================================================
# 1️⃣ For Loop
# ============================================================
print("=== For Loop ===")
fruits = ['apple', 'banana', 'cherry']
for f in fruits:
    print("Fruit:", f)

# Using range
for i in range(3):
    print("Index:", i)

# ============================================================
# 2️⃣ While Loop
# ============================================================
print("\n=== While Loop ===")
count = 1
while count <= 3:
    print("Count:", count)
    count += 1

# ============================================================
# 3️⃣ Nested Loops
# ============================================================
print("\n=== Nested Loop ===")
for i in range(2):
    for j in range(3):
        print(f"i={i}, j={j}")

# ============================================================
# 4️⃣ Break, Continue, Pass
# ============================================================
print("\n=== Break, Continue, Pass ===")
for i in range(5):
    if i == 2:
        continue   # skips 2
    if i == 4:
        break      # stops loop at 4
    print("Value:", i)
else:
    print("Loop finished without break")

# Pass example
for i in range(3):
    pass  # placeholder
print("Pass example executed\n")

# ============================================================
# 5️⃣ For...Else Loop
# ============================================================
print("=== For...Else Example ===")
for i in range(3):
    print(i)
else:
    print("Loop completed normally (no break)\n")

# ============================================================
# 6️⃣ Enumerate and Zip
# ============================================================
print("=== Enumerate and Zip ===")
names = ['Ali', 'Sara', 'Zain']
ages = [23, 21, 19]

# Enumerate gives index + value
for index, name in enumerate(names):
    print(f"Index={index}, Name={name}")

# Zip combines multiple lists
for n, a in zip(names, ages):
    print(f"{n} is {a} years old")

print("\n========== 'IN' AND 'NOT IN' IN PYTHON ==========\n")

# ============================================================
# 7️⃣ Plain Python Examples (Lists, Sets, Strings)
# ============================================================
fruits = ['apple', 'banana', 'cherry']
print("Fruit list:", fruits)

# Check single item
if 'mango' not in fruits:
    print("✅ Mango is not in the list")
else:
    print("❌ Mango is in the list")

# Find which items are not in fruits
items = ['apple', 'mango', 'orange']
missing = [x for x in items if x not in fruits]
print("Items not in fruits:", missing)

# Using 'in' with strings
word = "titanic"
if 'z' not in word:
    print("✅ Letter 'z' not found in word")

print("\n------------------------------------------------------------")

# ============================================================
# 8️⃣ Pandas Examples (DataFrame)
# ============================================================
print("=== Pandas DataFrame Examples ===")

df = pd.DataFrame({
    'Name': ['Ali', 'Sara', 'Ahmed', 'Zain', 'Laiba'],
    'Age': [25, 22, 28, 24, 21],
    'City': ['Lahore', 'Karachi', 'Islamabad', 'Lahore', 'Multan']
})
print("\nOriginal DataFrame:")
print(df)

# ============================================================
# 9️⃣ Using .isin() and ~ for "in" and "not in"
# ============================================================
in_cities = df[df['City'].isin(['Lahore', 'Karachi'])]
print("\n✅ Rows where City is in ['Lahore', 'Karachi']:")
print(in_cities)

not_in_cities = df[~df['City'].isin(['Lahore', 'Karachi'])]
print("\n❌ Rows where City is NOT in ['Lahore', 'Karachi']:")
print(not_in_cities)

# ============================================================
# 🔟 Using query() for same purpose
# ============================================================
in_query = df.query("City in ['Lahore', 'Karachi']")
print("\n✅ Using query(): City in ['Lahore', 'Karachi']")
print(in_query)

not_in_query = df.query("City not in ['Lahore', 'Karachi']")
print("\n❌ Using query(): City not in ['Lahore', 'Karachi']")
print(not_in_query)

# ============================================================
# 11️⃣ Multiple column example
# ============================================================
multi_filter = df[~df['Name'].isin(['Ali', 'Sara']) & ~df['City'].isin(['Lahore'])]
print("\n❌ Rows where Name not in ['Ali','Sara'] AND City not in ['Lahore']:")
print(multi_filter)

# ============================================================
# 12️⃣ Using Sets for Fast 'in' Checks
# ============================================================
print("\n=== Using Sets for Fast 'in' Checks ===")
numbers = {2, 4, 6, 8, 10}
test_values = [3, 4, 5, 10, 11]

for n in test_values:
    if n in numbers:
        print(f"{n} is in the set")
    else:
        print(f"{n} is NOT in the set")

print("\n✅ Script Completed Successfully ✅")
