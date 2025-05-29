import Demo
print(Demo.add(4,5))

#Or we can import like this and use this:
from Demo import add as a, mul as m
print(a(4,5),m(4,5))

#use of __name__ method
#output e demo show krbe jde na ami if else condition diye kicu set kore na dei
print(__name__)