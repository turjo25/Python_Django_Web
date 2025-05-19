#Bundling of data (attributes) and methods (functions) that operate on the data into a single unit, typically a class. It also restricts direct access to some components, which helps protect the integrity of the data and ensures proper usage.

#Public Members
class Public:
    def __init__(self):
        self.name = "John"  # Public attribute

    def display_name(self):
        print(self.name)  # Public method

obj = Public()
obj.display_name()  # Accessible
print(obj.name)  # Accessible

#Protected members(single underscore (_))
#--> accessed only within the class or its subclasses.
class Protected:
    def __init__(self):
        self._age = 30  # Protected attribute

class Subclass(Protected):
    def display_age(self):
        print(self._age)  # Accessible in subclass

obj = Subclass()
obj.display_age()

# Private members(double underscore (__))
#--> accessed only within the class.
class Private:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def salary(self):
        return self.__salary  # Access through public method

obj = Private()
print(obj.salary())  # Works
#print(obj.__salary)  # Raises AttributeError

    

    