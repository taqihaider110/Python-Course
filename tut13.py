import turtle             # allows us to use the turtles library
wn = turtle.Screen()      # creates a graphics window
wn.bgcolor("lightgreen")  # set the window background color
alex = turtle.Turtle()    # create a turtle named alex
alex.pensize(50)
alex.forward(150)         # tell alex to move forward by 150 units
alex.color("red")
alex.left(90)             # turn by 90 degrees
alex.forward(75)          # complete the second side of a rectangle
alex.color("blue")
alex.left(90)
alex.forward(150)
alex.color("yellow")
alex.left(90)
alex.forward(75)
alex.color("green")

wn.exitonclick()                # wait for a user click on the canvas
