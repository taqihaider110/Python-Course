import random

# Generating random numbers
print(random.random())        # Random float between 0 and 1
print(random.randint(1, 10))  # Random integer between 1 and 10

# Choosing random elements
my_list = [1, 2, 3, 4, 5]
print(random.choice(my_list))     # Randomly chosen element
print(random.sample(my_list, 3))  # List of 3 unique random elements

# Shuffling elements
random.shuffle(my_list)
print(my_list)  # Shuffled list

# Generating random numbers with a seed
random.seed(42)
print(random.random())  # Will always produce the same number
