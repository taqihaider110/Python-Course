def square(num):
    return num ** 2

print(square(3))
def sub(num1,num2):
    print(sub(square(num1),square(num2+1)))

sub(3,1)
