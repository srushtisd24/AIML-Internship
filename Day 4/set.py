set={1,2,3,4}
set.add(5)
print(set)
set.remove(3)
print(set)
set.discard(4)
print(set)

#set Operations
a={1,2,3}
b={4,5,6}
print(a | b)
print(a & b)
print(a - b) 
print(a ^ b)

if 1 in set:
    print("Exists")
else:
    print("not exist")


for i in set:
    print(i)
