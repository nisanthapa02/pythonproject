import turtle

scrn = turtle.Screen()
# turtle.screensize(canvwidth=1920, canvheight=1080)
pen = turtle.Turtle()

def goRight():
    if pen.heading() == 90.0:
        pen.right(90)
    else:
        pen.left(abs(0-pen.heading()))
    pen.forward(10)

def goLeft():
    if pen.heading() == 270.0:
        pen.right(90)
    else:
        pen.left(abs(180-pen.heading()))
    pen.forward(10)

def goDown():
    if pen.heading() == 0.0:
        pen.right(90)
    else:
        pen.left(abs(270-pen.heading()))
    pen.forward(10)

def goUp():
    if pen.heading() == 180.0:
        pen.right(90)
    else:
        pen.left(abs(90-pen.heading()))
    pen.forward(10)

turtle.listen()
turtle.onkeypress(goLeft, "Left")
turtle.onkey(goRight, "Right")
turtle.onkey(goUp, "Up")
turtle.onkey(goDown, "Down")

turtle.done()
