import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")


tess = turtle.Turtle()           # create tess and set his pen width
tess.pensize(5)

taqi = turtle.Turtle()           # create alex
taqi.color("hotpink")            # set his color

taqi.forward(80)                 # Let tess draw an equilateral triangle
taqi.left(120)
taqi.forward(80)
taqi.left(120)
taqi.forward(80)
taqi.left(120)                   # complete the triangle

tess.right(180)                  # turn tess around
tess.forward(80)                 # move her away from the origin so we can see alex

taqi.forward(50)                 # make alex draw a square
taqi.left(90)
taqi.forward(50)
taqi.left(90)
taqi.forward(50)
taqi.left(90)
taqi.forward(50)
taqi.left(90)

wn.exitonclick()
