# Take input from user below dictionary having name and age pair. Save this dictionary in
# json file. Now load this json file and Print name of person having maximum age and also
# print if anyone has the same age by making logic yourself without using any library:
# dictionary = {'Ali': 23,'Saad':24,'Salman':15,'Shams':25,'Sadiq':46,'Hammad':23'} Handle all
# possible exceptions as well.

import json

try:
    data = {}
    n = int(input("Enter number of people: "))
    for i in range(n):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        data[name] = age

    with open("data.json", "w") as f:
        json.dump(data, f)

    with open("data.json", "r") as f:
        loaded_data = json.load(f)

    max_age = max(loaded_data.values())
    print("Maximum age:", max_age)
    print("Person(s) with maximum age:")
    for k, v in loaded_data.items():
        if v == max_age:
            print(k)

    same_age = {}
    for k, v in loaded_data.items():
        same_age[v] = same_age.get(v, 0) + 1

    print("\nPeople having same age:")
    for age, count in same_age.items():
        if count > 1:
            print(f"Age {age} appears {count} times")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An unexpected error occurred:", e)
