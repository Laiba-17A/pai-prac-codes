# Create a program that reads a text file, searches for a 
# specified word or phrase, and replacesall occurrences with 
# another word or phrase. Write the modified content back to the file.

try:
    with open("file.txt", "r") as file:
        data=file.read()
        data=data.replace("hello", "hi")

    with open("file.txt", "w") as file:
        file.write(data)

except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print("An unexpected error occurred:", e)
