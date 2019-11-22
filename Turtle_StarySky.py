import turtle
from random import randint

#Setting up window
window = turtle.Screen()
window.title("Starry Sky")
turtle.bgcolor("black")

turtle.color("yellow")
turtle.speed(0)

def draw_star():

    turns = 5
    turtle.begin_fill()
    while turns >0:
        turtle.forward(25)
        turtle.left(145)
        turns = turns-1

    turtle.end_fill()

num_stars = 0
while num_stars <50:
    x = randint(-300,300)
    y = randint(-300,300)
    draw_star()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    num_stars = +1

turtle.done()