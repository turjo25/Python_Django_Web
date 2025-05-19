# 1. Method overriding-->
class GrandFather:
    def greet(self):
        print("GrandFather greets")
class Father(GrandFather):
    def greet(self): #overriding 
        print("Father greets")       
class Child(Father):
    def greet(self): #overriding
        print("Child greets")

# 2. Mthod Overloading
#Python does not support method overloading in the traditional sense as found in languages like Java or C++.
#However, it is possible to achieve similar functionality using techniques like default arguments, variable-length argument lists (*args and **kwargs), or conditional logic within a single method.
class Example:
    def method(self, arg1=None, arg2=None):
        if arg1 != None and arg2 != None:
            print("Two arguments:", arg1, arg2)
        elif arg1 != None:
            print("One argument:", arg1)
        else:
            print("No arguments")

obj = Example()
obj.method()
obj.method(10)
obj.method(10, 20)