import turtle
wn = turtle.Screen()
wn.bgcolor("light blue")
taqi=turtle.Turtle()
taqi.pensize(5)
taqi.color("red")
distance=50
angle=45

for _ in range(10):
    taqi.forward(distance)
    taqi.right(angle)
    angle-=10

wn.exitonclick()