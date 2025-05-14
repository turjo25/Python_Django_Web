#writing in file
#overwrites everything what was there before
with open('info.txt','w') as f:
    f.write("Hello, my name is Turjo\n")
    f.write("I am from fp\n")
    f.write("Currently in DIU")

#can also write list
lines = ["I am turjo\n","I am in fp\n","I am now in DIU\n"]
with open('info.txt','w') as f:
    f.writelines(lines)
