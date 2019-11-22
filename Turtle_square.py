import turtle

square = turtle.Turtle()

square.color("blue","cyan")

square.begin_fill()
for i in range(4):
    square.forward(100)
    square.left(90)

square.end_fill()

square.penup()
square.forward(150)
square.pendown()

square.begin_fill()
for i in range(4):
    square.forward(100)
    square.left(90)

square.end_fill()





turtle.done()