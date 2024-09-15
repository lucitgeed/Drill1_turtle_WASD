import turtle


def moveleft():
    turtle.penup()
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(50)
    turtle.stamp()

def moveright():
    turtle.penup()
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(50)
    turtle.stamp()

def moveup():
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def movedown():
    turtle.penup()
    turtle.setheading(270)
    turtle.pendown()
    turtle.forward(50)
    turtle.stamp()

def tothe_beginning():
    turtle.clear()
    turtle.penup()
    turtle.setheading(90)
    turtle.goto(0,0)


turtle.shape("turtle")


turtle.onkey(moveup,'w')
turtle.onkey(movedown, 's')
turtle.onkey(moveleft, 'a')
turtle.onkey(moveright, 'd')
turtle.onkey(tothe_beginning, 'Escape')

turtle.listen()


turtle.exitonclick()

