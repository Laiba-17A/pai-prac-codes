# Write a python program that takes any two lists from user havingsame number of elements.
# Make a dictionary from these two lists in such a way that first
# element of first list will be key and first element of second list
# will be its associated value and so on. Store the dictionary in a text file.
# Handle all possible exceptions as well. Note: do not use any library. Make logic yourself.

def create_dict():
    try:
        list1 = input("Enter elements of first list: ").split()
        list2 = input("Enter elements of second list ").split()
        list1 = [item.strip() for item in list1]
        list2 = [item.strip() for item in list2]

        if len(list1) != len(list2):
            print("Error: Both lists must have the same number of elements.")
            return

        my_dict = {}
        for i in range(len(list1)):
            my_dict[list1[i]] = list2[i]

        with open("dictionary.txt", "w") as file:
            for key, value in my_dict.items():
                file.write(f"{key} : {value}\n")
        print("Dictionary:", my_dict)

    except FileNotFoundError:
        print("Error: Unable to create or write to file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

create_dict()
