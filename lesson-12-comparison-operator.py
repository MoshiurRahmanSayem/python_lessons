
# Lesson 12: Comparison Operators
# This program compares two numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a == b:
    print(f"{a} and {b} are equal.")
elif a > b:
    print(f"{a} is greater than {b}.")
else:
    print(f"{b} is greater than {a}.")
