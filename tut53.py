fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']
print(alist)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []
print(alist)

alist = ['a', 'd', 'f']
alist[1:1] = ['b', 'c']
print(alist)
print(len(alist))
alist[4:4] = ['e']
print(alist)
