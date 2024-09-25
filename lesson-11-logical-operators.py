
# Lesson 11: Logical Operators
# This program checks if a number is within a range using logical operators

number = int(input("Enter a number: "))
if number >= 10 and number <= 50:
    print(f"{number} is between 10 and 50.")
else:
    print(f"{number} is not in the range.")
