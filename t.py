import turtle
turtle.shape("turtle")
turtle.color('red','blue')
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.end_fill()

turtle.exitonclick()