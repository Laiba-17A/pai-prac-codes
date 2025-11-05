# Take two integer numbers from user as input. Divide these two numbers. If one number is
# being divided by zero (another number) then handle ZeroDivisionError and if entered value
# is wrong (for example, a string) then handle ValueError.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integer numbers.")
except Exception as e:
    print("An unexpected error occurred:", e)
