# Write code to find out how many lines are in the file emotion_words.txt as shown above.
# Save this value to the variable num_lines. Do not use the len method.

f = open('emotion_words.txt', 'r')
num_lines = 0  # initialize counter for number of lines read from file
for char in f.read():
        if char == '\n':
            num_lines += 1

# Print the total number of lines in the file
print("Number of Lines:", num_lines)
        