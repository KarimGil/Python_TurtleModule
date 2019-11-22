import turtle
import math


circle = turtle.Turtle()
circle.color("green")
circle.speed(10)


for i in range(2000):
    circle.forward(math.sqrt(i))
    circle.left(i%180)

turtle.done()