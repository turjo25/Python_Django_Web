def squre(x):
    return x*x
print(squre(5))

#lambda function
squre = lambda x : x*x
print(squre(4)) 

students = [("Rahim",60),("Karim",49),("Fahim",100)]
sorted_students = sorted(students, key=lambda x:x[1]) #number wise aescending order sorting
print(sorted_students)

