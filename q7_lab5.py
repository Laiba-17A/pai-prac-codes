# You need to read "replacement_needed.txt" file. This file has one mistake. One letter needs
# to be replaced with other letter then this sentence might have some meaning. Replace this
# letter with the desired one making logic yourself without using any library. Write your code
# in function and call that function. Handle all possible exceptions as well.


def fix_file():
    try:
        with open("replacement_needed.txt", "r") as f:
            content = f.read()

        print("Original content:", content)

        corrected = ""
        for i in content:
            if i == "k":       
                corrected += "h"   # replace 'k' with 'h'
            else:
                corrected += i

        with open("replacement_needed.txt", "w") as f:
            f.write(corrected)

        print("Corrected content:", corrected)

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An unexpected error occurred:", e)

fix_file()
