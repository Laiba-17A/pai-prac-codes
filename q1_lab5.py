#Write a Python program that reads a text file, 
# counts the number of characters in it, and
#prints the total word count. Handle all possible exceptions as well.

def count(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            char_count = len(content)
            word_count = len(content.split())
            print("Total characters:", char_count)
            print("Total words:", word_count)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

count("file.txt")