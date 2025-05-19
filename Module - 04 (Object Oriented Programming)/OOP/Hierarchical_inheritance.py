class Vehicle:
    def engine_type(self):
        print("Vehicle has an engine")

class Car(Vehicle):
    def num_doors(self):
        print("Car has 4 doors")
class Truck(Vehicle):
    def load_capacity(self):
        print("load capacity is 10 tons")
car = Car()
car.engine_type()
truck = Truck()
truck.engine_type()

#Car and the Truck class inherited the same class --> this is called herarchial inheritancce