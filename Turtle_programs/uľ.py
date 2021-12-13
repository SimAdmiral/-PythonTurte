import turtle as t
import math
screen = t.Screen()

screen.setup(startx= 750, starty= 0)

def ul():
    num1 = int(input('take a number'))
    num = 0
    t.lt(90)
    x = 0
    t.speed(0)

    while num < num1:
        t.pd()
        n = 10
        t.color('black', 'yellow')
        for i in range(3):
            t.begin_fill()
            for i in range(6):
                t.fd(n)
                t.lt(360/6)
            t.lt(360/3)
            x += 1
            t.end_fill()

        print(x)
        if x%6 == 0:
            t.rt(-120)
            t.pu()
            t.fd(-n*3)
            t.lt(-120)
            n = 0
            print(x)

        if x%3 ==0:
            t.rt(120)
            t.pu()
            t.fd(n*3)
            t.lt(120)
        num += 1

ul()
t.done()
