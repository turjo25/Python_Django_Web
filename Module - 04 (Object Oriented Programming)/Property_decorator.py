class Employee:
    company_name = "Ostad Company"
    def __init__(self,name,salary):
        self.name = name
        self._salary = salary 

    #property decorator
    @property #--> its work like getter method also
    def salary(self):
        return self._salary
    
    #getter:
    #@property already makes salary accessible like a normal attribute (ob1.salary), so you don’t need a separate @salary.getter method.

    #setter:
    @salary.setter
    def salary(self, new_salary):
            self._salary = new_salary
    
ob1 = Employee("Rahmin",4000)
#getting salary
print(ob1.salary)

#setting salary
ob1.salary = 50000
print(ob1.salary)
