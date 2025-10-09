### Classes - Superclasses, Inheritance & Overriding.

class Animal:                                # Base/Super class: holds shared attributes and methods
    def __init__(self, species):             # Constructor for all animals
        self.species = species               # Store the species name as an attribute

    def speak(self):                         # Generic method (can be overridden)
        return f"{self.species} says hello"  # Default behaviour if not overridden

class Dog(Animal):                           # Subclass of Animal: overrides speak() with dog-specific behaviour
    def speak(self):                         # Method Override
        return "The dog says woof!"          # Replaces the Animal.speak method

class Cat(Animal):                           # Subclass of Animal: overrides speak() with cat-specific behaviour
    def speak(self):                         # Method Override
        return "The cat says meow!"          # Replaces the Animal.speak method

animals = [Dog("dog"), Cat("cat"), Dog("dog")] # Create a list of different Animal objects and their species (polymorphism in action)

for animal in animals:                       # Loop through and call speak() on each object
    print(animal.speak())                    # Each subclass responds in its own way
print(Cat(Animal).speak())

#=======================================================================================================================================================================================

import math

class Shape:
    def area(self):   # base method: guarantees all Shapes have .area()
        raise NotImplementedError("Subclass must implement area()")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

# List of different shapes
shapes = [Circle(5), Rectangle(4, 6), Circle(2)]

# Polymorphism in action
for shape in shapes:
    print(shape.area())

    # This showcases a major benefit of Superclasses, Rectangle does not have the area base method, so therefore it returns the NotImplementedError.
    # Without the superclass, I would have to trust that all shapes have their own area function, causing Python to raise the error, not me.

#=========================================================================================================================================================================

### LSP Rule and Violation example:

# LSP Rule states that any Function of a Superclass, must work with all of its descendants (subclasses)

class Bird:                     # Super class creation
    def fly(self):              # Base Method - Every Subclass is expected to have this method
        print("I can fly!")     # Output

class Penguin(Bird):                       # Subclass (descendant)
    def fly(self):                         # Base Method 
        raise Exception("I can't fly!")    # Raises an Exception instead of flying
    
def make_bird_fly(bird: Bird):             # Function, passing in bird 'Bird' is a convention suggesting that it should be of the subclass 'Bird'
    bird.fly()                             # Run the Base Method

penguin = Penguin()
eagle = Bird()

make_bird_fly(eagle)
make_bird_fly(penguin)








