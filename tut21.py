# import random
from random import random, randrange
# prob = random.random()
# print(prob)

# diceThrow = random.randrange(1,7)       # return an int, one of 1,2,3,4,5,6
# print(diceThrow)

prob = random()
print(prob)

diceThrow = randrange(1,7)       # return an int, one of 1,2,3,4,5,6
print(diceThrow)

# The `random` module in Python provides functions to generate random numbers and perform random operations. 
# It's commonly used for simulations, games, and various other applications that require randomness. 
# Here's a brief overview of some key functions and methods within the `random` module:

# 1. **Generating Random Numbers:**

#    - `random.random()`: Returns a random floating-point number in the range [0.0, 1.0).

#    - `random.randint(a, b)`: Returns a random integer in the range [a, b] inclusive.

#    - `random.uniform(a, b)`: Returns a random floating-point number in the range [a, b).

# 2. **Choosing Random Elements:**

#    - `random.choice(sequence)`: Returns a random element from the given sequence (list, tuple, string, etc.).

#    - `random.sample(population, k)`: Returns a list of k unique elements randomly chosen from the population sequence.

#    - `random.shuffle(sequence)`: Shuffles the elements of a sequence randomly in place.

# 3. **Generating Randomness with Seeds:**

#    - `random.seed(a=None, version=2)`: Initializes the random number generator with a seed value, which determines the sequence of random numbers.
#    Providing the same seed value will result in the same sequence of random numbers.

# 4. **Random Distributions:**

#    The `random` module also provides functions for generating random numbers following specific probability distributions, such as the normal distribution:

#    - `random.gauss(mu, sigma)`: Returns a random number following a Gaussian (normal) distribution with mean `mu` and standard deviation `sigma`.

#    - Other distribution functions include `random.expovariate(lambd)` for the exponential distribution and more.

# Remember to import the `random` module before using these functions:

# ```python
# import random

# # Generating random numbers
# print(random.random())        # Random float between 0 and 1
# print(random.randint(1, 10))  # Random integer between 1 and 10

# # Choosing random elements
# my_list = [1, 2, 3, 4, 5]
# print(random.choice(my_list))     # Randomly chosen element
# print(random.sample(my_list, 3))  # List of 3 unique random elements

# # Shuffling elements
# random.shuffle(my_list)
# print(my_list)  # Shuffled list

# # Generating random numbers with a seed
# random.seed(42)
# print(random.random())  # Will always produce the same number

# # Generating random numbers following a distribution
# print(random.gauss(0, 1))  # Random number from standard normal distribution
# ```

# Keep in mind that while these numbers are generated using algorithms, they are not truly random; they are pseudorandom, 
# meaning that they follow a deterministic sequence based on the seed. If you want to ensure true randomness, 
# you might need to use external sources like hardware random number generators.