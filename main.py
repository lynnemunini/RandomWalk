from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.shape("circle")
tim.shapesize(0.5, 0.5)
tim.width(11)
angles = [0, 90, 180, 270, 360]
# Can also use setheading() to pick a random direction
# side = [tim.left, tim.right]
tim.speed("fastest")


def move():
    x = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.pencolor(x)
    tim.fillcolor(x)
    tim.fd(20)


def direction():
    move()
    # my_side = random.choice(side)
    my_angle = random.choice(angles)
    # Using set heading
    tim.setheading(my_angle)
    # my_side(my_angle)


for _ in range(200):
    direction()


screen.exitonclick()

