from abc import ABC, abstractmethod

# Abstract parent class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass  
# Subclass Car implementing abstract methods
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with a key")

# Subclass Motorcycle implementing abstract methods
class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started with a button")

car = Car()
car.start_engine()  


motorcycle = Motorcycle()
motorcycle.start_engine()  
