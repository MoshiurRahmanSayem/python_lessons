
# Lesson 30: Constructor
# This program demonstrates a constructor

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

person1 = Person("John", 25)
person1.greet()
