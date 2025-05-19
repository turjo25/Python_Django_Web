class Employee:
    company_name = "Ostad Company"
    def __init__(self,name,salary):
        self.name = name
        self._salary = salary #_variable dara private variable bujhay but logically private na banayle private na
    #getter method:
    def get_salary(self,password):
        if password == "admin":
            print(self._salary)
        else:
            print("Invalid Password")
    #setter method
    def set_salary(self, password, salary):
        if password == "admin":
            self._salary = salary
            # print(f"New salary: {salary}")
        else:
            print("Invalid Password")
        

ob1 = Employee("Rahmin",4000)
print(ob1._salary) #access kora jabe karon logically akhn o private kora hoy nai
ob1.set_salary("admin",5000)
ob1.get_salary("admin")


    

    