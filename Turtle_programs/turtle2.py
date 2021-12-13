import turtle
import random

turtle.window_width()
turtle.speed(0)

#--------------------------------------------------
left = False
right = True
left1 = False
right1 = False
#--------------------------------------------------

do = 0
x = int(input('how many lines?'))

while True:

    while left:
        turtle.colormode(255)
        turtle.width(5)  # Width in pixels of the lines drawn (constant)
        r = random.randint(0, 255) #COLOR1
        g = random.randint(0, 255) #COLOR2
        b = random.randint(0, 255) #COLOR3
        turtle.pencolor([r, g, b]) #COLOR MODE
        turtle.forward(10)
        pos = turtle.pos()

        if pos <= (-100, 0):
            do += 1
            if do >= x:
                left = False
                right = False
                right1 = True
                left1 = False
                dio = 0
            else:
                turtle.right(90)
                turtle.forward(10)
                turtle.right(90)
                left = False
                right = True

    while right:
        turtle.colormode(255)
        turtle.width(5)  # Width in pixels of the lines drawn (constant)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.pencolor([r, g, b])
        turtle.forward(10)
        pos = turtle.pos()
        if pos >= (100, 0):
            do += 1

            if do >= x:
                left = False
                right = False
                left1 = True
                right1 = False
                do = 0
            else:
                turtle.left(90)
                turtle.forward(10)
                left = True
                right = False
                turtle.left(90)

    while left1:
        turtle.color('black')
        turtle.bk(10)
        pos = turtle.pos()

        if pos <= (-100, 0):
            do += 1
            if do >= x:
                print('done')
                turtle.done()
            left1 = False
            right1 = True
            turtle.left(90)
            turtle.bk(10)
            turtle.left(90)


    while right1:
        turtle.color('red')
        turtle.bk(10)
        pos = turtle.pos()

        if pos >= (100,0):
            do += 1
            if do >= x:
                print('done')
                turtle.done()
            left1 = True
            right1 = False
            turtle.right(90)
            turtle.bk(10)
            turtle.right(90)

