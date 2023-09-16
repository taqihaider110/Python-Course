# Given that we want to accumulate the total number of strings in the list,
# which of the following accumulator patterns would be appropriate?
lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
s = 0
for item in lst:
    if type(item) == type("string"):
        s = s + 1
        
print(s)