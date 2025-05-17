class Car:
    def __init__(self,brand,model): 
        self.brand = brand
        self.model = model
    def display_info(self):
        print(f"Car Brand: {self.brand}\nCar Model: {self.model}")

car1 = Car("Toyota","Crown")
car1.display_info()
    