import turtle
import random

turtle.speed('fastest')
x = 5
kolko = int(input('how many brick do you want? ')) * 4
run2 = False
run1 = True
number = 0
while True:
    while run1:

        turtle.colormode(255)

        turtle.width(2)  # Width in pixels of the lines drawn (constant)

        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        turtle.pencolor([r,g,b])

        turtle.forward(x)
        turtle.right(90)
        x += 2
        number += 1
        if number >= kolko:
            run2 = True
            break
    number = 0
    while run2:
        turtle.width(8)  # Width in pixels of the lines drawn (constant)
        turtle.pencolor('black')
        turtle.forward(x)
        turtle.right(90)
        x += 2
        number += 1
        if number >= 4:
            run2 = False
            run1 = True
            break
turtle.done()
