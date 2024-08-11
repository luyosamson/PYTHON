# Task 1: Create Base Classes
# Create two base classes, Person and 
# Employee, each with its own __init__ method that initializes an attribute and prints a message.
# Task 2: Create a Derived Class
# Create a derived class Manager that inherits from both Person and Employee. 
# Ensure that the Manager class properly initializes both base classes using both explicit calls and super().
# Task 3: Demonstrate MRO
# Print the Method Resolution Order (MRO) for the Manager class.
# Task 4: Creating Instances and Testing
# Create instances of the Manager class and another class that demonstrates the 
# diamond problem, and call their methods to ensure everything works as expected.
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
class Employee:
    def __init__(self,id,position):
        self.id=id
        self.position=position
    def infor(self):
        print(f'Your ID is {self.id}, position {self.position}')
class Manager(Person,Employee):
    def __init__(self,name,age,gender,id,position,team_size):
        Person.__init__(self,name,age,gender)
        Employee.__init__(self,id,position)
  
        self.team_size=team_size

    def infor(self):
        print(f'Name {self.name}, position {self.position} team size {self.team_size}')
m=Manager("Samson",34,"Male",674,"CTO,5",9)
print(m.name)
print(Manager.__mro__)
