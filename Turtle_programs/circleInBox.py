import turtle as t
import random
import math
t.speed(0)
x = 0
while x < 50:
    x += 1
    t.circle(50, 90)
    t.circle(-50, 90)
    t.circle(50, 90)
    t.circle(50, -90)
    t.circle(-50, -90)
    t.circle(50, -90)
    t.left(360/50)
t.dot(150, 'yellow')
t.pu()
t.fd(220)
t.left(90)
t.pd()
t.pensize(4)
t.pencolor('yellow')
t.speed('normal')
t.circle(220)
t.pu()
t.home()
t.pensize(1)
t.pd()

a = 0
t.speed(0)
t.color('black')
while a < 20:
   t.circle(20)
   t.left(360/20)
   a += 1
a = 0
while a < 20:
   t.color('red')
   for i in range(4):
       t.fd(20)
       t.left(90)
   a += 1
   t.left(360/20)

t.done()
