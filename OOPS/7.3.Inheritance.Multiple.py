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

class PetOwner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def display_all_pets_info(self):
        print(f"\nPets owned by {self.name}:")
        for pet in self.pets:
            pet.display_info()

    def interact_with_pets(self):
        print(f"\nInteractions with pets by {self.name}:")
        for pet in self.pets:
            pet.speak()

# Objects
generic_animal = Animal("Generic Animal", 5)
buddy = Dog("Buddy", 3, "Golden Retriever")
whiskers = Cat("Whiskers", 2, "Gray")

# Pet owner and interactions
john = PetOwner("John")
john.add_pet(generic_animal)
john.add_pet(buddy)
john.add_pet(whiskers)

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

# Pet owner interactions
john.display_all_pets_info()
john.interact_with_pets()


# In this more advanced example:

# The PetOwner class uses composition to manage a collection of pets.
# The add_pet method allows adding pets to the owner's collection.
# The display_all_pets_info method displays information about all owned pets.
# The interact_with_pets method interacts with each pet by calling their speak method.
# When you run this code, you'll see output that includes information about each pet, their specific actions, and the interactions with the pet owner:
