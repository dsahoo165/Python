# Base class
class Animal:
    def __init__(self, name):
        print("_init_ called: "+ name)
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Derived class 1
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

# Derived class 2
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

# Objects
animal_generic = Animal("Generic Animal")
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Using the classes
print("Generic Animal:")
animal_generic.speak()

print("\nDog:")
dog.speak()

print("\nCat:")
cat.speak()
