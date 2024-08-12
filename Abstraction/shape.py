from abc import ABC,abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return self.l*self.w
    def perimeter(self):
        return 2*(self.l+self.w)
    
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.142*self.r**2
    def perimeter(self):
        return 2*3.142*self.r
    
r1=Rectangle(10,10)
print(r1.area())
    