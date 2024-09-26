import turtle
from turtle import left, right, backward, forward
turtle.speed(8)

turtle.up()
turtle.goto(0,-150)
turtle.down()

# I think 0 is best, but 5, 10, and 15 all work, too.
angle = 0

# This can be anything, depending on how big you want the star to be. 
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

    def draw_big_again(color):
        turtle.color(color)
        turtle.up()
        right(angle)
        backward(15)
        right(5)
        turtle.down()
        draw_star(side,5)

    draw_big_again("blue")
    draw_big_again("green")
    draw_big_again("cyan")

draw_big_star()


# Similar to above, this can be any number. For example, 30, 80, and 160.
side = 100

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
        backward(5)
        right(5)
        turtle.down()
        draw_star(side,5) 

    draw_small_layers("red")
    draw_small_layers("magenta")
    draw_small_layers("purple")

def draw_many_small(number):
    for i in range (number):
        turtle.up()
        turtle.goto(0,30)
        right(44+i)
        forward(240)
        turtle.down()
        draw_small_star()

draw_many_small(6)


turtle.exitonclick()