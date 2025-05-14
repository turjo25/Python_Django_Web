# for multiple arguments --> *args
def addition(*args):
    print(args)
    return sum(args)

res = addition(10,11,12,13)
print(res)