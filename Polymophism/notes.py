import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement this method")

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

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

def print_area(shape):
    print(f"The area of the shape is: {shape.area()}")

# Creating instances of different shapes
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)
triangle = Triangle(base=3, height=7)

# Calling the same function with different shapes
print_area(circle)      # Output: The area of the shape is: 78.53981633974483
print_area(rectangle)   # Output: The area of the shape is: 24
print_area(triangle)    # Output: The area of the shape is: 10.5


# Explanation
# Base Class (Shape):

# Shape is an abstract base class that defines a method area() which is
#  meant to be overridden by subclasses. It raises a NotImplementedError if not implemented in a subclass.
# This class is not intended to be instantiated directly but serves as a template for other shapes.

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement this method")
# Derived Classes:Circle,Rectangle and Triangel

# 
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

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Polymorphic Function (print_area):

# The print_area() function takes an object of type Shape (or any subclass of Shape) and calls its area() method.
# This function works with any object that has an area() method, regardless of its specific class.

def print_area(shape):
    print(f"The area of the shape is: {shape.area()}")
# Usage:

# We create instances of Circle, Rectangle, and Triangle.
# We then call print_area() with these different objects.
# Even though Circle, Rectangle, and Triangle are different classes, the print_area() 
# function can handle them all because they share a common interface (area() method).

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)
triangle = Triangle(base=3, height=7)

print_area(circle)      # Output: The area of the shape is: 78.53981633974483
print_area(rectangle)   # Output: The area of the shape is: 24
print_area(triangle)    # Output: The area of the shape is: 10.5


# Key Concepts:
# Polymorphism: The print_area() function is polymorphic, meaning it can accept any object 
# that implements the area() method, regardless of the object's class.
# Method Overriding: Each subclass (Circle, Rectangle, 
# Triangle) overrides the area() method to provide its specific implementation.
# Common Interface: All shapes share a common interface (the area() method), allowing 
# them to be used interchangeably in the print_area() function.