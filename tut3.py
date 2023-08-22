def square(num):
    return num ** 2

print(square(3))

def sub(num1, num2):
    return num1 - num2

result = sub(square(3), square(1 + 1))
print(result)
