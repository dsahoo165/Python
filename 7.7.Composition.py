# In this more advanced example, we'll introduce the concept of composition with interfaces, and we'll implement a more elaborate system involving a Veterinary Clinic that can perform health checks on pets. We'll also use exception handling to handle potential errors:

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self._breed = breed

    @property
    def breed(self):
        return self._breed

    def speak(self):
        return f"{self.name} the {self.breed} barks"

    def display_info(self):
        return f"Dog - Name: {self.name}, Age: {self.age}, Breed: {self.breed}"

    def fetch(self):
        return f"{self.name} fetches the ball"

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color

    @property
    def color(self):
        return self._color

    def speak(self):
        return f"{self.name} the {self.color} cat meows"

    def display_info(self):
        return f"Cat - Name: {self.name}, Age: {self.age}, Color: {self.color}"

    def climb_tree(self):
        return f"{self.name} climbs the tree"

class VeterinaryClinic:
    def __init__(self, name):
        self._name = name
        self._patients = []

    @property
    def name(self):
        return self._name

    def admit_patient(self, patient):
        if isinstance(patient, Animal):
            self._patients.append(patient)
            print(f"{patient.name} admitted to {self.name} Veterinary Clinic.")
        else:
            print(f"{patient} is not a valid patient!")

    def perform_health_check(self):
        print(f"\nHealth check at {self.name} Veterinary Clinic:")
        for patient in self._patients:
            try:
                if isinstance(patient, Animal):
                    print(f"Performing health check for {patient.name}: {patient.speak()}")
                else:
                    raise ValueError(f"Invalid patient type: {type(patient).__name__}")
            except Exception as e:
                print(f"Error during health check: {e}")

# Objects
buddy = Dog("Buddy", 3, "Golden Retriever")
whiskers = Cat("Whiskers", 2, "Gray")

# Veterinary Clinic
vet_clinic = VeterinaryClinic("Paws and Claws")

# Admitting pets to the clinic
vet_clinic.admit_patient(buddy)
vet_clinic.admit_patient(whiskers)

# Performing health checks
vet_clinic.perform_health_check()





# In this more advanced example:

# A new class, VeterinaryClinic, is introduced to demonstrate composition. The VeterinaryClinic class can admit patients (animals) and perform health checks on them.
# The perform_health_check method uses exception handling to handle potential errors during the health check process, providing a more robust approach.
# When you run this code, you'll see output demonstrating composition, exception handling, and more advanced interactions:

# sql
# Copy code
# Buddy admitted to Paws and Claws Veterinary Clinic.
# Whiskers admitted to Paws and Claws Veterinary Clinic.

# Health check at Paws and Claws Veterinary Clinic:
# Performing health check for Buddy: Buddy the Golden Retriever barks
# Performing health check for Whiskers: Whiskers the Gray cat meows

# This example demonstrates more advanced concepts such as composition, exception handling, and a more modular system for managing different types of objects in a veterinary clinic scenario


# plz explain concept of composition with interfaces
#---------------------------------------------------------
# Composition is a design principle in object-oriented programming where a class contains objects of other classes, allowing you to build more complex functionality by combining simpler components. In the context of composition with interfaces, the goal is to define a set of interfaces (abstract classes with abstract methods) that can be implemented by various classes. These interfaces represent the contracts that classes must adhere to, ensuring a certain level of common behavior.

# Let's break down the concept of composition with interfaces using the Veterinary Clinic example:

# 1.Animal Interface:

# python
# Copy code
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass

#     @abstractmethod
#     def display_info(self):
#         pass
# The Animal interface defines two abstract methods: speak and display_info. Any class that wants to be considered an Animal must implement these methods.

# 2.Concrete Animal Classes:

# python
# Copy code
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} the {self.breed} barks"

#     def display_info(self):
#         return f"Dog - Name: {self.name}, Age: {self.age}, Breed: {self.breed}"

# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} the {self.color} cat meows"

#     def display_info(self):
#         return f"Cat - Name: {self.name}, Age: {self.age}, Color: {self.color}"
# The Dog and Cat classes implement the Animal interface. They provide specific implementations for the speak and display_info methods, ensuring that they fulfill the contract defined by the Animal interface.

# 3.VeterinaryClinic Class:

# python
# Copy code
# class VeterinaryClinic:
#     def __init__(self, name):
#         self._name = name
#         self._patients = []

#     def admit_patient(self, patient):
#         if isinstance(patient, Animal):
#             self._patients.append(patient)
#             print(f"{patient.name} admitted to {self.name} Veterinary Clinic.")
#         else:
#             print(f"{patient} is not a valid patient!")

#     def perform_health_check(self):
#         print(f"\nHealth check at {self.name} Veterinary Clinic:")
#         for patient in self._patients:
#             try:
#                 if isinstance(patient, Animal):
#                     print(f"Performing health check for {patient.name}: {patient.speak()}")
#                 else:
#                     raise ValueError(f"Invalid patient type: {type(patient).__name__}")
#             except Exception as e:
#                 print(f"Error during health check: {e}")
# The VeterinaryClinic class takes advantage of composition by having a list of Animal patients. It has methods like admit_patient and perform_health_check that interact with these patients. The clinic doesn't need to know the specific details of each animal class, only that they adhere to the common Animal interface.

# In this way, composition with interfaces allows you to create a flexible and modular system. You can easily extend the system by adding new classes that implement the Animal interface without modifying the existing code. This promotes code reuse, maintainability, and a clear separation of concerns.