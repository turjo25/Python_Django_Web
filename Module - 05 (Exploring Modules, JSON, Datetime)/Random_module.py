import random
# help(random)
# print(dir(random))
# print(random.__doc__)
# print(random.random()) 0-1 er moddhe shb random value dibe
# print(random.uniform(5,10))
# print(random.randint(1,100))
# print(random.randrange(1,100,5))

#Operations on a list
fruits = ['apple','mango','banana']
print(random.choice(fruits))

random.shuffle(fruits)
print(fruits)

def generate_pin():
    return random.randint(1000,9999)

print(f"Random pin is: {generate_pin()}")


