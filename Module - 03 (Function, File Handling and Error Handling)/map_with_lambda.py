nums = [1,2,3,4,5]
st = list(map(str,nums))
print(st)
fl = list(map(float,nums))
print(fl)

#map using lambda
sq_nums = list(map(lambda x:x*x,nums))
print(sq_nums)
