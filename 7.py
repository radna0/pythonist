# Class definition
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name, "says woof!")

# Object instantiation
my_dog = Dog("Buddy", 3)
my_dog.bark()
