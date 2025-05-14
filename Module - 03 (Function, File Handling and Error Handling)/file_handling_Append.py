#writing in file (append)
#not overwrites everything just adds in the last
with open('info.txt','a') as f:
    f.write("I am learning python\n")
    f.write("This is file handling\n")

#can also append list
lines = ["Python is so good\n","I am enjoying it\n","I love coding\n"]
with open('info.txt','a') as f:
    f.writelines(lines)