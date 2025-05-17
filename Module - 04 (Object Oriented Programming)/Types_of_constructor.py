class Car:
    #default constructor:
    def __init__(self): 
        self.brand = ''
        self.model = ''
    #parameterized consturctor:
    def __init__(self,brand,model): 
        self.brand = brand
        self.model = model
    #default value constructor:
    def __init__(self,brand = "Toyota",model = "Crown"): 
        self.brand = brand
        self.model = model


car1 = Car()
car1.brand = "Honda"
car1.model = "Civic"
print(car1.brand,car1.model)

car2 = Car()
print(car2.brand,car2.model)