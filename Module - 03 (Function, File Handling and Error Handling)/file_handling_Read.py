#Read from file
file = open('file.txt','r')
content = file.read()
print(content)

#Short:
with open('file.txt','r') as f:
    print(file.read())


