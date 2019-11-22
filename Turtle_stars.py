import turtle

stars = turtle.Turtle()
stars.getscreen().bgcolor("#994444")
stars.penup()
stars.forward(150)
stars.pendown()


def star(turtle,size):
    for i in range(5):
        turtle.backward(size)
        turtle.left(216)

star(stars,200)



turtle.done()