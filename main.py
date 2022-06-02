import turtle
import random
t = turtle.Turtle()
t.penup()
t.goto(-300, -259.80762)
t.pendown()
t.dot(5)
t.penup()
t.forward(600)
t.pendown()
t.dot(5)
t.left(120)
t.penup()
t.forward(600)
t.pendown()
t.dot(5)
t.left(120)
t.penup()
t.speed(10000000000000000000000000000000000000000000000)
t.forward(random.randint(0, 600))
t.hideturtle()
for x in range(1000000000000000000000000000):

    point = random.randint(1, 3)
    if point == 1:
        def travel1(x, y):
            xPos = x + -300
            xPos = xPos / 2
            yPos = y + -259.80762
            yPos = yPos / 2
            t.goto(xPos, yPos)
            t.pendown()
            t.dot(2)
            t.penup()


        travel1(t.xcor(), t.ycor())
    elif point == 2:
        def travel1(x, y):
            xPos = x + 300
            xPos = xPos / 2
            yPos = y + -259.80762
            yPos = yPos / 2
            t.goto(xPos, yPos)
            t.pendown()
            t.dot(2)
            t.penup()


        travel1(t.xcor(), t.ycor())
    elif point == 3:
        def travel1(x, y):
            xPos = x + 0
            xPos = xPos / 2
            yPos = y + 259.80762
            yPos = yPos / 2
            t.goto(xPos, yPos)
            t.pendown()
            t.dot(2)
            t.penup()


        travel1(t.xcor(), t.ycor())

turtle.done()
