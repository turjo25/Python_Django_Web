# txt = "For only {price:} dollars!"
# print(txt.format(price = 49))
# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# print(txt1)
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# print(txt2)
# txt3 = "My name is {}, I'm {}".format("John",36)
# print(txt3)

name_inp = input("what is your name? ")
age_inp = input("what is your age?: ")

name = "My name is {} and I am {} years old".format(name_inp,age_inp)
print(name)

#longtech:
name = "My name is {n} and I am {a} years old".format(n=name_inp,a=age_inp)
print(name)

#shortcut
name = f"My name is {name_inp} and I am {age_inp} years old"
print(name)

