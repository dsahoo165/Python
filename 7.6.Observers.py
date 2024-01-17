#  In this advanced example, we'll introduce the concept of composition over inheritance and demonstrate a design pattern called the Observer Pattern. We'll create a PetObserver class that observes changes in pets and notifies the owner about those changes. Additionally, we'll use type hints for function parameters and return values:

from abc import ABC, abstractmethod
from typing import List, Optional

# Observer pattern: Observer class
class PetObserver(ABC):
    @abstractmethod
    def update(self, pet_name: str, action: str):
        pass

# Observer pattern: Concrete Observer class
class PetOwnerObserver(PetObserver):
    def update(self, pet_name: str, action: str):
        print(f"{pet_name} did {action}. Owner notified!")

class Pet(ABC):
    def __init__(self, name: str, age: int, observers: Optional[List[PetObserver]] = None):
        self._name = name
        self._age = age
        self._observers = observers or []

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @abstractmethod
    def speak(self) -> None:
        pass

    @abstractmethod
    def display_info(self) -> None:
        pass

    def add_observer(self, observer: PetObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: PetObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, action: str) -> None:
        for observer in self._observers:
            observer.update(self.name, action)

class Dog(Pet):
    def __init__(self, name: str, age: int, breed: str, observers: Optional[List[PetObserver]] = None):
        super().__init__(name, age, observers)
        self._breed = breed

    @property
    def breed(self) -> str:
        return self._breed

    def speak(self) -> None:
        print(f"{self.name} the {self.breed} barks")

    def display_info(self) -> None:
        print(f"Dog - Name: {self.name}, Age: {self.age}, Breed: {self.breed}")

    def fetch(self) -> None:
        print(f"{self.name} fetches the ball")
        self.notify_observers("fetching")

class Cat(Pet):
    def __init__(self, name: str, age: int, color: str, observers: Optional[List[PetObserver]] = None):
        super().__init__(name, age, observers)
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    def speak(self) -> None:
        print(f"{self.name} the {self.color} cat meows")

    def display_info(self) -> None:
        print(f"Cat - Name: {self.name}, Age: {self.age}, Color: {self.color}")

    def climb_tree(self) -> None:
        print(f"{self.name} climbs the tree")
        self.notify_observers("climbing a tree")

class Robot:
    def __init__(self, model: str):
        self._model = model

    @property
    def model(self) -> str:
        return self._model

    def move(self) -> None:
        print(f"{self.model} moves to a new location")

    def charge(self) -> None:
        print(f"{self.model} is charging")

class PetOwner(Robot, PetObserver):
    def __init__(self, name: str, robot_model: str, observers: Optional[List[PetObserver]] = None):
        super().__init__(robot_model)
        self._name = name
        self._pets: List[Pet] = []
        self._observers = observers or []

    @property
    def name(self) -> str:
        return self._name

    def add_pet(self, pet: Pet) -> None:
        if isinstance(pet, Pet):
            pet.add_observer(self)
            self._pets.append(pet)
        else:
            print(f"{pet} is not a valid pet!")

    def display_all_pets_info(self) -> None:
        print(f"\nPets owned by {self.name}:")
        for pet in self._pets:
            pet.display_info()

    def interact_with_pets(self) -> None:
        print(f"\nInteractions with pets by {self.name}:")
        for pet in self._pets:
            pet.speak()

    def find_pet_by_name(self, pet_name: str) -> Optional[Pet]:
        for pet in self._pets:
            if pet.name == pet_name:
                return pet
        print(f"No pet with the name {pet_name} found.")
        return None

    def update(self, pet_name: str, action: str) -> None:
        print(f"Notification: {self.name} received an update - {pet_name} did {action}.")

# Objects
buddy = Dog("Buddy", 3, "Golden Retriever")
whiskers = Cat("Whiskers", 2, "Gray")

# Pet owner and interactions
john = PetOwner("John", "PetBot")
john.add_observer(PetOwnerObserver())
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

# Additional functionality: Finding a pet by name
found_pet = john.find_pet_by_name("Buddy")
if found_pet:
    print(f"\nFound a pet: {found_pet.name} the {type(found_pet).__name__}")





# In this advanced example:

# The Observer Pattern is introduced using the PetObserver and PetOwnerObserver classes. The PetOwner class is both a Robot and a PetObserver.
# Type hints are used for function parameters and return values for better code readability and clarity.
# The concept of composition over inheritance is demonstrated by allowing PetOwner to observe pets without inheriting from them.
# When you run this code, you'll see output demonstrating the Observer Pattern, composition over inheritance, and advanced features:

    # yaml
    # Copy code
    # Dog:
    # Dog - Name: Buddy, Age: 3, Breed: Golden Retriever
    # Buddy the Golden Retriever barks
    # Buddy fetches the ball
    # Notification: John received an update - Buddy did fetching. Owner notified!

    # Cat:
    # Cat - Name: Whiskers, Age: 2, Color: Gray
    # Whiskers the Gray cat meows
    # Whiskers climbs the tree
    # Notification: John received an update - Whiskers did climbing a tree. Owner notified!

    # Pets owned by John:
    # Dog - Name: Buddy, Age: 3, Breed: Golden Retriever
    # Cat - Name: Whiskers, Age: 2, Color: Gray

    # Interactions with pets by John:
    # Buddy the Golden Retriever barks
    # Whiskers the Gray cat meows

    # PetBot moves to a new location
    # PetBot is charging

    # Found a pet: Buddy the Dog
# This example showcases advanced concepts such as the Observer Pattern, composition over inheritance, type hints, and more sophisticated interactions between classes.



# In the journey of advancing your understanding of Python and object-oriented programming (OOP), you can explore various advanced concepts and patterns. Here are some suggestions for what you can explore next:

# Design Patterns: Learn about common design patterns in software development. Some popular ones include Singleton, Factory, Observer, Decorator, and Strategy patterns. Understanding these patterns can enhance your ability to design scalable and maintainable software.

# Metaclasses: Explore metaclasses, which allow you to customize class creation in Python. Metaclasses are an advanced feature and are used to modify the behavior of class creation itself.

# Descriptors: Understand descriptors, which are a powerful way to customize attribute access in Python classes. Descriptor protocols include __get__, __set__, and __delete__.

# Multiple Inheritance: Delve deeper into multiple inheritance, its challenges, and how to use it effectively. Understand the Method Resolution Order (MRO) and the super() function.

# Abstract Base Classes (ABCs): Learn about Abstract Base Classes and how they provide a way to define interfaces in Python. The abc module provides tools for creating and working with ABCs.

# Mixins: Explore mixins, a technique that allows you to create modular and reusable pieces of functionality that can be combined in various ways.

# Context Managers: Understand context managers using the with statement. You can create your own context managers by implementing __enter__ and __exit__ methods.

# Generators and Coroutines: Learn about generators for lazy evaluation and coroutines for asynchronous programming. Explore the async and await keywords for writing asynchronous code.

# Type Annotations and Type Hints: Dive into type annotations and type hints, introduced in Python 3.5+. This allows you to add optional static typing to your Python code, enhancing code readability and maintainability.

# Unit Testing and Test-Driven Development (TDD): Explore unit testing frameworks like unittest or pytest and practice test-driven development. Writing tests before writing code can lead to more robust and maintainable software.

# Memory Management: Understand Python's memory management, garbage collection, and best practices for managing memory efficiently.

# Performance Optimization: Learn about techniques for optimizing the performance of your Python code, including profiling, code optimization, and the use of specialized libraries.

# Remember that advancing your skills is a gradual process, and it's essential to apply what you learn through practical projects and real-world scenarios. Experimenting with these advanced concepts in your coding projects will deepen your understanding and proficiency in Python programming.
