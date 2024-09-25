
# Lesson 31: Inheritance
# This program demonstrates inheritance

class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")

dog = Dog()
dog.speak()
