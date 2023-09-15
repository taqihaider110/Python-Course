# Write code to create a list of integers from 0 through 52 
# and assign that list to the variable numbers. You should 
# use the Python range function and don’t forget to covert the result to a list
# – do not type out the whole list yourself.
numbers = list(range(53))

    # Count the number of characters in string str1. Do not use len(). Save the number in variable numbs.


str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
numbs=0
for i in str1:
    numbs+=1
    
print(numbs)

# Create a list of numbers 0 through 40 and assign this list to the variable numbers. 
# Then, accumulate the total of the list’s values and assign that sum to the variable sum1.

numbers = list(range(41))  # Create a list of numbers from 0 to 40
sum1 = 0  # Initialize the sum variable

for num in numbers:
    sum1 += num  # Accumulate the total

print(sum1)
