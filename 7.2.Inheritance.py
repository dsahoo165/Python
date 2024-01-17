class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} makes a generic sound")

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print(f"{self.name} the {self.breed} barks")

    def fetch(self):
        print(f"{self.name} fetches the ball")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(f"{self.name} the {self.color} cat meows")

    def climb_tree(self):
        print(f"{self.name} climbs the tree")

# Objects
generic_animal = Animal("Generic Animal", 5)
buddy = Dog("Buddy", 3, "Golden Retriever")
whiskers = Cat("Whiskers", 2, "Gray")

# Using the classes
print("Generic Animal:")
generic_animal.display_info()
generic_animal.speak()

print("\nDog:")
buddy.display_info()
buddy.speak()
buddy.fetch()

print("\nCat:")
whiskers.display_info()
whiskers.speak()
whiskers.climb_tree()



# In this advanced example:

# Both Dog and Cat classes have their own specific attributes (breed for Dog and color for Cat).
# Each derived class has its own speak method, which overrides the method in the base class.
# Additional methods (fetch for Dog and climb_tree for Cat) demonstrate how subclasses can extend the functionality of the base class.
# When you run this code, you should see output that includes information about each animal, along with their specific actions: