#Octagon Shape for turtle
import turtle
wn=turtle.Screen()
wn.bgcolor("Light Blue")
taqi=turtle.Turtle()
taqi.color("red")
taqi.pensize(5)
taqi.shape("turtle")
taqi.speed(1)
for _ in range(8):
    taqi.forward(100)
    taqi.stamp()
    taqi.right(45)
    
wn.exitonclick()
