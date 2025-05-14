# raise keyword use kore custom exceotion banano jay
def check_file(filename):
    if not filename.endswith(".txt"):
        raise ValueError("Only txt are allowed")
    print("Valid file")


try:
    check_file("data.txt")
except Exception as e:
    print(e)
