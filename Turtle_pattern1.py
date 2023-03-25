import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

turtle.bgcolor('black')


for x in range(360):
    turtle.speed(10000)
    turtle.pencolor(colors[x%2])#2,5,7
    turtle.forward(x)
    turtle.left(59)