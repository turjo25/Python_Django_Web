def my_fun(f_name,l_name,age):
    print(f"My name is {f_name} {l_name}. I am {age} years old")

my_fun(f_name = "Rahim",l_name="khan",age=25)

#emon aro onkgula arguments ashle,
def my_fun(**kwargs):
    print(kwargs)
    print(f"My name is {kwargs['f_name']} {kwargs['l_name']}. I am {kwargs['age']} years old. I am currently in {kwargs['address']}. I am a {kwargs['occupation']}")

my_fun(f_name = "Rahim",l_name="khan",age=25,address = "Dhaka",occupation = "student")