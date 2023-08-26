import turtle
wn=turtle.Screen()
wn.bgcolor("lightblue")
taqi=turtle.Turtle()
taqi.color("red")
taqi.pensize(5)
taqi.shape("turtle")
taqi.penup()
taqi.speed(1)
for _ in range(10):
    taqi.forward(50)
    taqi.stamp()
    taqi.forward(-50)
    taqi.right(36)
      
wn.exitonclick() 