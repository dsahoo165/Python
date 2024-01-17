from abc import ABC, abstractmethod

class Pet(ABC):
    def __init__(self, name, age):
        self._name = name  # Encapsulation: Use a single leading underscore to indicate it's a protected attribute
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

class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self._breed = breed

    @property
    def breed(self):
        return self._breed

    def speak(self):
        print(f"{self.name} the {self.breed} barks")

    def display_info(self):
        print(f"Dog - Name: {self.name}, Age: {self.age}, Breed: {self.breed}")

    def fetch(self):
        print(f"{self.name} fetches the ball")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color

    @property
    def color(self):
        return self._color

    def speak(self):
        print(f"{self.name} the {self.color} cat meows")

    def display_info(self):
        print(f"Cat - Name: {self.name}, Age: {self.age}, Color: {self.color}")

    def climb_tree(self):
        print(f"{self.name} climbs the tree")

class Robot:
    def __init__(self, model):
        self._model = model

    @property
    def model(self):
        return self._model

    def move(self):
        print(f"{self.model} moves to a new location")

    def charge(self):
        print(f"{self.model} is charging")

class PetOwner(Robot):
    def __init__(self, name, robot_model):
        super().__init__(robot_model)
        self._name = name
        self._pets = []

    @property
    def name(self):
        return self._name

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            self._pets.append(pet)
        else:
            print(f"{pet} is not a valid pet!")

    def display_all_pets_info(self):
        print(f"\nPets owned by {self.name}:")
        for pet in self._pets:
            pet.display_info()

    def interact_with_pets(self):
        print(f"\nInteractions with pets by {self.name}:")
        for pet in self._pets:
            pet.speak()

    def find_pet_by_name(self, pet_name):
        for pet in self._pets:
            if pet.name == pet_name:
                return pet
        print(f"No pet with the name {pet_name} found.")

    @classmethod
    def create_pet_owner(cls, name, robot_model):
        print(f"Creating a new PetOwner named {name} with a {robot_model} robot.")
        return cls(name, robot_model)

# Objects
buddy = Dog("Buddy", 3, "Golden Retriever")
whiskers = Cat("Whiskers", 2, "Gray")

# Pet owner and interactions
john = PetOwner.create_pet_owner("John", "PetBot")
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





# In this more advanced example:

# Encapsulation is introduced by using a single leading underscore to indicate protected attributes.
# Properties (@property decorator) are used to provide controlled access to the attributes.
# A class method (@classmethod decorator) is used to create a PetOwner instance with additional setup.
# When you run this code, you'll see output demonstrating encapsulation, properties, and class methods:



# Properties:
# In Python, properties allow you to define getter, setter, and deleter methods for class attributes. This is useful for controlling access to the attributes and performing additional actions when the attribute is accessed, modified, or deleted. The @property decorator is used to create a read-only property.

# In the provided example:

# python
# Copy code
# class Pet(ABC):
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age
# Here, the name and age attributes are marked as properties using the @property decorator. These properties have only a getter method, meaning you can access them like attributes, but they cannot be directly modified or deleted. The leading underscore in _name and _age conventionally indicates that these attributes are intended to be protected.

# When you create an instance of the Pet class, you can access the name and age attributes as if they were regular attributes, but they are, in fact, being accessed through the getter methods:

# python
# Copy code
# pet_instance = Pet("Fido", 4)
# print(pet_instance.name)  # Accessing the 'name' property
# print(pet_instance.age)   # Accessing the 'age' property



# Class Methods:
# A class method is a method bound to the class and not the instance of the class. It takes the class itself as the first argument, often named cls. The @classmethod decorator is used to define a class method.

# In the provided example:

# python
# Copy code
# class PetOwner(Robot):
#     def __init__(self, name, robot_model):
#         super().__init__(robot_model)
#         self._name = name
#         self._pets = []

#     @property
#     def name(self):
#         return self._name

#     @classmethod
#     def create_pet_owner(cls, name, robot_model):
#         print(f"Creating a new PetOwner named {name} with a {robot_model} robot.")
#         return cls(name, robot_model)
# Here, the create_pet_owner method is marked as a class method using the @classmethod decorator. This method is responsible for creating and returning a new instance of the PetOwner class. Note that it takes the class itself (cls) as the first parameter, which allows it to create instances of the class.

# When you call this class method:

# python
# Copy code
# john = PetOwner.create_pet_owner("John", "PetBot")
# It prints a message indicating the creation and returns a new PetOwner instance with the specified name and robot model.

# In summary, properties and class methods provide additional control and flexibility in defining and interacting with classes. Properties help in controlling access to attributes, while class methods provide a way to perform actions related to the class itself, not just an instance of the class.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



## what are the additional capabilities of john = PetOwner.create_pet_owner("John", "PetBot") compared to buddy = Dog("Buddy", 3, "Golden Retriever")
# Answer:
# The create_pet_owner class method in the PetOwner class provides an alternative way to create an instance of the PetOwner class compared to directly instantiating it using the constructor (__init__) method. Let's discuss the additional capabilities and differences between the two approaches:

# 1.Initialization and Additional Setup:

    # Direct Instantiation (buddy = Dog("Buddy", 3, "Golden Retriever")):
    # When you directly instantiate an object, the initialization logic is handled by the constructor (__init__) method.
    # You provide the necessary parameters at the time of instantiation ("Buddy", 3, "Golden Retriever").
    # Class Method (john = PetOwner.create_pet_owner("John", "PetBot")):
    # The class method create_pet_owner allows for additional setup or custom logic during object creation.
    # It can perform actions beyond simple attribute assignment, as demonstrated by the print statement ("Creating a new PetOwner...").

# 2.Flexibility in Object Creation:

    # Direct Instantiation (buddy = Dog("Buddy", 3, "Golden Retriever")):
    # Direct instantiation provides a straightforward way to create an object with specific parameters.
    # Class Method (john = PetOwner.create_pet_owner("John", "PetBot")):
    # The class method can encapsulate more complex logic or actions related to object creation.
    # It allows for more flexibility in the process of creating and initializing objects.

# 3.Return Value:

    # Direct Instantiation (buddy = Dog("Buddy", 3, "Golden Retriever")):
    # The instance buddy is directly assigned the newly created Dog object.
    # Class Method (john = PetOwner.create_pet_owner("John", "PetBot")):
    # The class method can return the created object or perform other actions. In this case, it returns the newly created PetOwner instance.
    # In summary, the create_pet_owner class method provides a more controlled and potentially customizable way to create instances of the PetOwner class. It allows for additional setup and logic during object creation, providing a more flexible and encapsulated approach compared to direct instantiation. The choice between these approaches depends on the specific requirements and complexity of the object creation process.



