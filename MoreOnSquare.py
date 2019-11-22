import turtle


#Setting up window
window = turtle.Screen()
window.title("More On Square")
turtle.speed(3)
turtle.pensize(5)
turtle.write("More On Square", font= (30))

#Outline of square

turtle.penup()
turtle.goto(-350,100)
turtle.pendown()
turtle.color("black")

for i in range(4):
    turtle.forward(150)
    turtle.left(90)


#Square two
turtle.penup()
turtle.goto(-175,100)
turtle.pendown()
turtle.color("red")

for i in range(4):
    turtle.forward(150)
    turtle.left(90)

#Multi color stroke
color = ['red','purple','yellow','blue']
turtle.penup()
turtle.goto(0,100)
turtle.pendown()
for colours in color:
    turtle.color(colours)
    turtle.forward(150)
    turtle.left(90)
turtle.penup()

#Filled color
turtle.penup()
turtle.goto(175,100)
turtle.pendown()
turtle.color("blue","cyan")
turtle.begin_fill()
for j in range(4):
    turtle.forward(150)
    turtle.left(90)
turtle.end_fill()


turtle.done()
