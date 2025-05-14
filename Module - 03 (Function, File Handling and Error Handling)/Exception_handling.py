# Exception --> Run time
# try:
#     with open('rahim.txt','r') as f:
#         print(f.read)
# except FileNotFoundError:
#     print("File not found")

# Multiple try catch
try:
    with open("file.txt", "r") as f:
        print(f.read())
        print(10 / 1)
        print(int("abc"))
        a = [1, 2, 3]
        print(a[100])
except FileNotFoundError:
    print("File not found")
except ZeroDivisionError:
    print("Can't divide by zero")
except ValueError:
    print("Invalid value")
except IndexError:
    print("Invalid index")

# If we don't know the name of exception
try:
    x = abc
except Exception as e:
    print("Something error! :", e)

# Using else:
try:
    x = abc
except Exception as e:
    print("Something error! :", e)
else:
    print("Code successfully executed")

# Using finally:
try:
    x = abc
except Exception as e:
    print("Something error! :", e)
finally:
    print("Eita print hbei")
