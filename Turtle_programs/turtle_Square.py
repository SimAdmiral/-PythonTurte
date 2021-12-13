import turtle
import random
import math


import turtle as t
x = 4
a = int(input('how many bricks do you want? '))
num = 0
run1 = True
run2 = False
t.pensize(3)

while run1:
    t.forward(x)
    x += 4
    num += 1

    if num >= a * 4:
        run1 = False
        num  = 0
        run2 = True
        t.left(180)
        t.pencolor('red')
        x1 = x
        break
    t.left(90)

while run2:
    x -= 4
    t.forward(x)
    t.right(90)
    num += 1

    if num >= a * 4:
        run2 = False
        run1 = False
        pos = t.pos()
        break

t.pu()
t.forward(4)
t.left(90)
t.pd()
x = 4
num = 0

while True and num <= a * 4 * 2:
    t.color('black')
    t.forward(x)
    x += 4
    t.left(90)
    num += 1

t.pu()
t.fd(4)
t.left(90)
t.pd()
t.color('green')
pos1 = t.pos()
x -= 8
k = 0
t.forward(4)

while True:
    x -= 4
    t.fd(x)
    t.right(90)

    if x <= x1:
        print('готово')
        break

t.done()
