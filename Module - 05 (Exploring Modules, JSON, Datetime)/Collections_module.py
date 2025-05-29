import collections
# print(collections.__doc__)
# print(dir(collections))

fruits = ['apple','banana','apple','orange','banana']
# print(collections.Counter(fruits))
# print(collections.Counter(fruits).most_common(2))

#we can import it like this
from collections import defaultdict as ddc

word_dict = ddc(list)
word_dict['Python'].append("Programming Language")
print(word_dict)

