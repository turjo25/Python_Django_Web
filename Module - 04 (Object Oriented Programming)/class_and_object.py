#Car class and properties of a car -> brand and model
class Car:
    def __init__(self): #constructor
        self.brand = ''
        self.model = ''

#Object
car1 = Car()
car1.brand = "Toyota"
car1.model = "Crown"
print(car1.brand,car1.model)

car2 = Car()
car2.brand = "Honda"
car2.model = "Civic"
print(car2.brand,car2.model)