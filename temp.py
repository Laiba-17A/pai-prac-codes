

print("Hello, World!")
file=open("example.txt", "w")
file.write("This is an example file.")
file.close()

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

with open("example.txt","a") as file:
    file.write("\nAppending a new line.")

with open("example.txt", "r") as file:
    content = file.readline()
    print(content)

import os
os.remove("example.txt")
print("File deleted.")

print(os.path.isfile("example.txt"))


import json
data = {"name": "Alice", "age": 30, "city": "New York"}
json_string = json.dumps(data)
print(json_string)
parsed_data = json.loads(json_string)
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

import numpy as np
array = np.array([1, 2, 3, 4, 5])
print(array)
print(array.mean())
print(array.std())
print(array.sum())
print(array.max())
print(array.min())
print(array.shape)
reshaped_array = array.reshape((5, 1))
print(reshaped_array)
transposed_array = reshaped_array.T
print(transposed_array)
sliced_array = array[1:4]
print(sliced_array)
filtered_array = array[array > 2]
print(filtered_array)



