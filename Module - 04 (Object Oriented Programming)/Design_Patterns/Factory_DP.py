class Bike:
    def driver(self):
        return "Diving a bike"
class Car:
    def driver(self):
        return "Diving a car"
class VeichleFactory:
    @staticmethod
    def get_vhicle(type):
        if type == "car":
             return Car()
        elif type == "bike":
            return Bike()
        else:
            return ValueError("Invalid option")

v1 = VeichleFactory.get_vhicle("car")
print(v1.driver())
    