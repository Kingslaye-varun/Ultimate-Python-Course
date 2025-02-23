s = {1, 5, 32, 54,"Varun"}

p = {8,11,54}

print(s, type(s))

s.add(566)  
print(s, type(s))

print(len(s))
s.remove(32)
print(s)

s.pop()
print(s)

# s.clear()
# print(s)
print(s.union(p))
print(s.intersection(p))