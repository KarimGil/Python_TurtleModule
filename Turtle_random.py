import turtle
import math


spinner = turtle.Turtle()
spinner.color("blue","cyan")
spinner.speed(1000)

spinner.begin_fill()
for i in range(1000):
    spinner.forward(10)
    spinner.left(math.sin(i/10)*25)
    spinner.left(20)
spinner.end_fill()
turtle.done()