a = "tuRjo rahman"
print(a.title())#Converts the first character of each word to upper case
print(a.upper())
print(a.lower())
print(a.swapcase())#Swaps cases, lower case becomes upper case and vice versa

t = "i love apple"
print(t.replace("apple","mango"))
print(t.count('a'))


#.rstrip
txt = "    banana     "
x = txt.rstrip()
print("of all fruits",x, "is my favorite")