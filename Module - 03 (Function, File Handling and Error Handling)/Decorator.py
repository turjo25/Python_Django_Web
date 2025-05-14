def my_decorator(f):
    def wrapper():
        print("Before")
        f()
        print("After")
    return wrapper

@my_decorator
def say_hello(): #ei function f e pass krce @my_decorator diye
    print("hi there")

say_hello()