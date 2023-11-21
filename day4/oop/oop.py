class Car:
    # Constructor / Initialization method
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to display car details
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

    def display_info(self, a,b):
        print(a, b)
    _wheels = 4
   

  

car1 = Car("bmw", "x3", "2020")
print(car1.make)

car1.display_info()
car1.display_info(10, 20)

# encapsulation
# property
# method
# access modifier => property + descriptor

#inhertance

#polymorphism

car1 = Truck()