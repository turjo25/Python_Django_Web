import functools
nums = [1,2,3,4,5]
sum = functools.reduce(lambda x,y : x+y,nums)
print(sum)