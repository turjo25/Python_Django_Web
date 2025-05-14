# a = [10,20,37,40,52,53]
# result = []
# # for i in a:
# #     if i%2 == 0:
# #         result.append(i)
# # print(result)

# #list comprehension of this code:
# result = [i for i in a if i%2==0]
# print(result)

#suppose we need the squre of even numbers only
b = [1,2,3,4,5]
b_new = []
# #without list comp
# for i in b:
#     if i%2==0:
#         b_new.append(i**2)
#     else:
#         b_new.append(i)
# print(b_new)
#with list comp
b_new = [i**2 if i%2==0 else i for i in b]
print(b_new)

