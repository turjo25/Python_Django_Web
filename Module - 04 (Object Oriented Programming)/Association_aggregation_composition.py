#Association: class can be exist without depending each other
class Laptop:
    def __init__(self,brand):
        self.brand = brand

class Student:
    def __init__(self,name,lp_obj):
        self.name = name
        self.lp_v = lp_obj
    def show_laptop_info(self):
        print(f"{self.name} has a laptop which brand is {self.lp_v.brand}")

lp1 = Laptop("Accer")
st1 = Student("Turjo",lp1)
st1.show_laptop_info()

#Aggregation: has a relationship 
#classes can operate independently
class Department:
    def __init__(self,name):
        self.name = name

class University:
    def __init__(self,name):
        self.name = name
        self.departments = []
    def add_depatments(self,department):
        self.departments.append(department)
    def show_departments(self):
        return [department.name for department in self.departments]

uni = University("DIU")
dp1 = Department("CSE")
dp2 = Department("SWE")
uni.add_depatments(dp1)
uni.add_depatments(dp2)
print(uni.show_departments())

#Composition: a class cannot exist without each other
class Engine:
    def __init__(self,power):
        self.power = power

class Car:
    def __init__(self,brand,power):
        self.brand = brand
        self.engine = Engine(power) #engine class has no value without car class
    def show_info(self):
        print(f"{self.brand} has an engine with power : {self.engine.power} HP")
        
car = Car("BMW",2100)
car.show_info()        