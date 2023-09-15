b = "My, what a lovely day"
x = b.split(',')
z = "".join(x)
y = z.split()
a = "".join(y)
print(a)

# Using split() and join() methods
# The split() method will break the given string by the specified separator
# and return a list of strings. The str separator is used by the join() 
# method to connect the elements of a sequence into a string.