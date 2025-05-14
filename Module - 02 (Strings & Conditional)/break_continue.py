# #break
# a = [1,2,3,4,'a',5,6,7]
# for i in a:
#     if type(i) == type('b'):
#         break #string type paile e break
#     else:
#         print(i)

a = [1,2,3,4,'a',5,6,7]
for i in a:
    if type(i) == type('b'):
        continue #string bad e shb print hbe
    else:
        print(i)