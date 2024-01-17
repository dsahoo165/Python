from abc import ABC, abstractmethod

# Abstract class or interface
class Pet(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

# Concrete class implementing the Pet interface
class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print(f"{self.name} the {self.breed} barks")

    def display_info(self):
        print(f"Dog - Name: {self.name}, Age: {self.age}, Breed: {self.breed}")

    def fetch(self):
        print(f"{self.name} fetches the ball")

# Another concrete class implementing the Pet interface
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(f"{self.name} the {self.color} cat meows")

    def display_info(self):
        print(f"Cat - Name: {self.name}, Age: {self.age}, Color: {self.color}")

    def climb_tree(self):
        print(f"{self.name} climbs the tree")

# Another class demonstrating multiple inheritance
class Robot:
    def __init__(self, model):
        self.model = model

    def move(self):
        print(f"{self.model} moves to a new location")

    def charge(self):
        print(f"{self.model} is charging")

# Enhanced PetOwner class using multiple inheritance
class PetOwner(Robot):
    def __init__(self, name, robot_model):
        super().__init__(robot_model)
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            self.pets.append(pet)
        else:
            print(f"{pet} is not a valid pet!")

    def display_all_pets_info(self):
        print(f"\nPets owned by {self.name}:")
        for pet in self.pets:
            pet.display_info()

    def interact_with_pets(self):
        print(f"\nInteractions with pets by {self.name}:")
        for pet in self.pets:
            pet.speak()

# Objects
buddy = Dog("Buddy", 3, "Golden Retriever")
whiskers = Cat("Whiskers", 2, "Gray")

# Pet owner and interactions
john = PetOwner("John", "PetBot")
john.add_pet(buddy)
john.add_pet(whiskers)

# Using the classes
print("\nDog:")
buddy.display_info()
buddy.speak()
buddy.fetch()

print("\nCat:")
whiskers.display_info()
whiskers.speak()
whiskers.climb_tree()

# Pet owner interactions
john.display_all_pets_info()
john.interact_with_pets()

# Robot actions
john.move()
john.charge()


# In this more advanced example:

# The Pet class is an abstract class (or interface) that defines abstract methods speak and display_info. Both Dog and Cat classes inherit from this abstract class, and they must implement these abstract methods.
# The Robot class is introduced to demonstrate multiple inheritance. The PetOwner class now inherits from both Robot and PetOwner, showing how a class can inherit from multiple parent classes.
# The PetOwner class now takes a robot_model parameter in its constructor to specify the model of the robot it owns.
# When you run this code, you'll see output demonstrating the use of abstract classes, multiple inheritance, and more complex interactions:



# The line from abc import ABC, abstractmethod in Python is importing two entities (ABC and abstractmethod) from the abc module, which stands for "Abstract Base Classes." Let me explain each part:

# ABC (Abstract Base Class):

# ABC is a metaclass provided by the abc module. It stands for Abstract Base Class.
# In Python, an abstract base class is a class that cannot be instantiated on its own and is meant to be subclassed by other classes. It defines a common interface for its subclasses.
# The ABC metaclass is used to create abstract base classes. By inheriting from ABC, a class is marked as an abstract base class.
# abstractmethod:

# abstractmethod is a decorator provided by the abc module.
# When applied to a method in an abstract base class, it indicates that the method is abstract and must be implemented by concrete (non-abstract) subclasses.
# Abstract methods are methods that are declared in the abstract base class but do not provide an implementation. Subclasses must override these methods.
# So, by using from abc import ABC, abstractmethod, you're importing the tools needed to define abstract base classes and abstract methods in your code. This becomes useful when you want to create a common interface for a group of related classes, ensuring that certain methods must be implemented by all subclasses. The use of abstract classes helps in achieving a level of abstraction and design consistency in your code.
