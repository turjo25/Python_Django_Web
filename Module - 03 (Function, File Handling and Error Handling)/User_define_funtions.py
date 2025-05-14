#No input + no return
def my_first_fun():
    a = 10
    b = 12
    print(a+b)

my_first_fun() #--> function call

#input + no return
def add_two_num(a,b):
    print(a+b)

add_two_num(5,10)

#input + return
def mul(a,b):
    return a*b

m = mul(10,5)
print(m)

#No input + return
def hello():
    return "Hello"

g = hello()
print(g)