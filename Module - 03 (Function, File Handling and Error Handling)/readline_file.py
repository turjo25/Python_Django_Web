with open('file.txt', 'r') as file:
    lines = file.readlines() #readlines diye file er shob line ek sathe read hoye jabe
    
for line in lines:
     print(line.strip()) #strips diye whitespace remove kore
