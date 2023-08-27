# Write code to draw a regular pentagon (a five-sided figure with all sides the same length).
import turtle
wn=turtle.Screen()
wn.bgcolor("Light Blue")
taqi=turtle.Turtle()
taqi.color("red")
taqi.pensize(5)
taqi.shape("turtle")
taqi.speed(1)
for _ in range(5):
    taqi.stamp()
    taqi.right(108-36)
    taqi.forward(100)
    
wn.exitonclick()