import turtle

flower = turtle.Turtle()
flower.color("red","yellow")
flower.speed(10)

flower.begin_fill()
for i in range(50):
    flower.forward(200)
    flower.left(170)

flower.end_fill()

turtle.done()