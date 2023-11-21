class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"{self.make} {self.model} - Vehicle")

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def display_info(self):
        print(f"{self.make} {self.model} {self.year} - Car")

car = Car("Toyota", "Corolla", 2022)
car.display_info()  # Output: Toyota Corolla 2022 - Car
super(Car, car).display_info()