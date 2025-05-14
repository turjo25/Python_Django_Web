l = []
while 1:
    items = input("Add any item:")
    if(items == "done"):
        break
    l.append(items)
print("Items are: ",l)
print("Total number of items: ",len(l))
    