n = "global" # global variable
def outer():
    # global n --> dile global er n change hoye enclosing hocce ajonno eita global change korte pare, enclosing na
    n = "enclosing" #enclosing variable
    def inner():
        # nonlocal n --> dile enclosing change hoye local hoy ajonno eita enclosing k change korte pare
        n = "Local" #local variable
        print(n)
    inner()
    print(n)
outer()
print(n)