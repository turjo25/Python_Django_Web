def generator_example():
    nums = [0,1,2,3,4,5]
    for numbers in nums:
        yield numbers

for val in generator_example():
    print(val)