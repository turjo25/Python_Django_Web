nums = [1,2,3,4,5]
even = list(filter(lambda x : x%2==0,nums))
print(even)
odd = list(filter(lambda x : x%2==1,nums))
print(odd)