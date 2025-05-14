a = {'rahim':12,'karim':13,'fahim':78,1:[1,2,3],2:{1,2,3,4}}
print(type(a))
#loop diye print
for i in a:
    print(i)#just key gulo access krbe

for i in a.values():
    print(i) #values use krce ajonno value pabo just

print(a.keys(),a.values())#keys trpor valuse

for k,v in a.items():
    print(f"keys: {k}, values: {v}")#keys,value akare dekhabe

#ZIP function
a = [1,2,3]
b = ["Mango","Banana","Apple"]
c = dict(zip(a,b))
print(c)

#can access only values using key
print(c[1])