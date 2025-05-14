# a = [1,2,3,4,5]
# result = 0
# i = 0
# n = len(a)
# while i<n:
#     result = result + a[i]
#     i+=1
# print(result)

#replace negative number with 0
a = [-10,2,19,-3,-5]
i = 0
while i<len(a):
    if a[i]<0:
        a[i]=0
    i+=1
print(a)