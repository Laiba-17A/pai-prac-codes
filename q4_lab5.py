# Take biodata of employee from user as Name, cnic number, age, and salary save it in txt
# file. Now append this file to add contact number. Finally read this file. Handle all possible
# exceptions as well.

try:
    name = input("Enter name: ")
    cnic = input("Enter cnic: ")
    age = input("Enter age: ")
    salary = input("Enter salary: ")

    with open("employee.txt", "w") as f:
        f.write(name + "\n")
        f.write(cnic + "\n")
        f.write(age + "\n")
        f.write(salary + "\n")

    contact = input("Enter contact number: ")
    with open("employee.txt", "a") as f:
        f.write(contact + "\n")

    with open("employee.txt", "r") as f:
        print("\nFile content:\n", f.read())

except FileNotFoundError:
    print("Error:file not found")

except Exception as e:
    print("An unexpected error occurred:", e)
