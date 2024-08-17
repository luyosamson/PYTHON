class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return "Engine started with horsepower: {}".format(self.horsepower)

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car "has-a" Engine
    
    def start(self):
        return f"{self.make} {self.model}: {self.engine.start()}"

# Creating an Engine instance
engine = Engine(150)

# Creating a Car instance and passing the Engine instance to it
car = Car("Toyota", "Corolla", engine)

# Starting the car, which in turn starts the engine
print(car.start())