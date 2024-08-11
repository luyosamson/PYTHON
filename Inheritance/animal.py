# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some generic sound"

# Derived class (Single Inheritance)
class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def sound(self):
        return "Some mammal sound"

# Another Base class
class Bird:
    def __init__(self, wing_span):
        self.wing_span = wing_span

    def fly(self):
        return "Flies in the sky"

# Derived class (Multiple Inheritance)
class Bat(Mammal, Bird):
    def __init__(self, name, fur_color, wing_span):
        Mammal.__init__(self, name, fur_color)
        Bird.__init__(self, wing_span)

    def sound(self):
        return "Screech"

# Further derived class (Hierarchical Inheritance)
class FruitBat(Bat):
    def __init__(self, name, fur_color, wing_span, favorite_fruit):
        super().__init__(name, fur_color, wing_span)
        self.favorite_fruit = favorite_fruit

    def sound(self):
        return "Chirp"

# Creating an object of FruitBat
fruit_bat = FruitBat("Eddy", "Brown", "1.5 meters", "Mango")
print(fruit_bat.name)  # Inherited from Animal class
print(fruit_bat.fur_color)  # Inherited from Mammal class
print(fruit_bat.wing_span)  # Inherited from Bird class
print(fruit_bat.favorite_fruit)  # Specific to FruitBat class
print(fruit_bat.sound())  # Overridden in FruitBat class
print(fruit_bat.fly())  # Inherited from Bird class
