
class Engine:
    def __init__(self):
        self.engine_type = "V8"
        print("Engine initialized")

class Body:
    def __init__(self):
        self.body_type = "Sedan"
        print("Body initialized")

class Car(Engine, Body):
    def __init__(self):
        Engine.__init__(self)
        Body.__init__(self)
        print("Car initialized")
    
    def display_features(self):
        print(f"Engine: {self.engine_type}, Body: {self.body_type}")

class Car(Engine, Body):
    def __init__(self):
        super().__init__()
        print("Car initialized")
    
    def display_features(self):
        print(f"Engine: {self.engine_type}, Body: {self.body_type}")

class Vehicle:
    def __init__(self):
        self.vehicle_type = "Generic Vehicle"
        print("Vehicle initialized")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.car_type = "Sedan"
        print("Car initialized")

class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.truck_type = "Pickup"
        print("Truck initialized")

class AmphibiousVehicle(Car, Truck):
    def __init__(self):
        super().__init__()
        print("Amphibious Vehicle initialized")
    
    def display_features(self):
        print(f"Vehicle: {self.vehicle_type}, Car: {self.car_type}, Truck: {self.truck_type}")


car = Car()  
car.display_features()  

amphibious_vehicle = AmphibiousVehicle()  
amphibious_vehicle.display_features()  
