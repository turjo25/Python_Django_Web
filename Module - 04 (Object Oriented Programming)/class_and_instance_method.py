class Employee:
    company_name = "ostad company"
    
    def __init__(self,name,salary): 
        self.name = name
        self.salary = salary
    
    def display_info(self): #instance method
        print(f"Emp name: {self.name}\nEmp salary: {self.salary}")
    
    @classmethod
    def change_company_name(cls,name): #class method
        cls.company_name = name
    

ob1 = Employee("Rahmin",3000)
print(ob1.company_name)
ob1.display_info()

Employee.change_company_name("XYZ company")
print(ob1.company_name) #er por theke shb object er company name chnage hoye xyz thakbe


    

    
