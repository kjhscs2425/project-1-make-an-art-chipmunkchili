import turtle
from turtle import left, right, backward, forward

turtle.speed(10)

turtle.up()
turtle.goto(0,-150)
turtle.down()

# I think 0 is best, but 5, 10, and 15 all work, too.
angle = 0

# This can be anything, depending on how big you want the large star to be. 
# Some options are 100, 200, and 400.
side = 325

def draw_big_star():
    global angle
    def draw_star(side, points):
        angle = 360/points
        for i in range(points):
            left(angle)
            forward(side)
            left(angle)
    draw_star(side,5)

    def draw_big_layers(color):
        turtle.color(color)
        turtle.up()
        right(angle)
        backward(12)
        right(4)
        turtle.down()
        draw_star(side,5)

    draw_big_layers("blue")
    draw_big_layers("green")
    draw_big_layers("cyan")

draw_big_star()


# Like above, this can be any number. It changes the size of the small star.
# For example, 30, 80, and 160.
side = 80

def draw_small_star():
    turtle.color("black")
    global angle
    def draw_star(side, points):
        angle = 360/points
        for i in range(points):
            left(angle)
            forward(side)
            left(angle)
    draw_star(side,5)


    def draw_small_layers(color):
        turtle.color(color)
        turtle.up()
        right(angle)
        backward(3)
        right(4)
        turtle.down()
        draw_star(side,5) 

    draw_small_layers("red")
    draw_small_layers("magenta")
    draw_small_layers("purple")

def draw_many_small(number):
    for i in range (number):
        turtle.up()
        turtle.goto(0,30)
        turtle.setheading(0)
        right((360/number)*i)
        forward(240)
        turtle.down()
        draw_small_star()

#Changing this parameter changes the number of small stars.
#Some other examples are be 6, 15, and 18 (but can be any).
draw_many_small(10)

turtle.exitonclick()