print("Hello, World!")
print(5 + 4)
print("All finished!")

import turtle
import math
wn = turtle.Screen()
bob = turtle.Turtle()
bob.right(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.speed(1)
bob.left(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
distance= math.sqrt(50*50/2)
bob.right(135)
bob.forward(distance)
bob.right(90)
bob.forward(distance)
wn.exitonclick()
# Add your code below!
