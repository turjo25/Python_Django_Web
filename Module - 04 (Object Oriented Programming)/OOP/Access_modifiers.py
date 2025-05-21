# Example of access modifiers
class Example:
    #public: accessible from anywhere
    public_var = "I am public"

    #protected: accessible from inside the class and also from the subclass
        #--> in python we can access this from anywhere but this is not a good practice
    _protected_var = "I am protected"

    #private: only accessible within class.
    __private_var = "I am private"

# Example:
class BankAccount:
    def __init__(self):
        self.__balance = 0 # Private
        self._type = "Savings" # Protected
    
    def addMoney(self,amount):
        self.__balance += amount
    
    def showBalance(self):
        print("Balance is: ",self.__balance)

ac = BankAccount()
ac.addMoney(500000)
ac.showBalance()