class Engine:
    def __init__(self,horsepower):
        self.horsepower=horsepower
    def start(self):
        return(f"horsepower: {self.horsepower}")
class  Car:
    def __init__(self,make,model,engine):
        self.make=make
        self.model=model
        self.engine=engine
    def info(self):
        print(f'The car is of make {self.make},of model {self.model} has a horsepower of {self.engine.horsepower}')

engine=Engine(200)
car1=Car("Premio","Pk4",engine)
car1.info()
# print(engine.horsepower)
    