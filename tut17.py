import turtle
wn = turtle.Screen()
wn.bgcolor("light blue")
taqi=turtle.Turtle()
taqi.pensize(5)
taqi.color("red")
distance=30
angle=45

for _ in range(10):
    taqi.forward(distance)
    taqi.right(angle)
    angle-=10
    
wasi=turtle.Turtle()
wasi.pensize(10)
wasi.color("Green")
distance=30
angle=45
wasi.left(180)
wasi.forward(distance)
for _ in range(10):
    wasi.forward(distance)
    wasi.left(angle)
    angle-=10

wn.exitonclick()