import turtle
import turtle as t
import math


def home():
    n = 100
    for i in range(4):
        t.fd(n)
        t.lt(90)

    t.lt(45)
    t.fd(math.sqrt(n**2 + n**2))
    t.lt(75)
    t.fd(math.sqrt(n**2 + n/2**2))
    t.lt(120)
    t.fd(math.sqrt(n**2 + n/2**2))
    t.lt(75)
    t.fd(math.sqrt(n**2 + n**2))

def squars():
    n = 100
    for i in range(4):
        t.fd(n)
        t.lt(90)

    t.right(90)
    t.fd(n)
    t.lt(90)
    t.fd(n)
    t.lt(90)
    t.fd(n)
    t.lt(90+45)
    t.fd(math.sqrt(n**2 + n**2))
    t.right(45)
    t.fd(n)
    t.right(90)
    t.fd(n)
    t.right(90)
    t.fd(n)
    t.right(90)

def squer_in():
    t.speed('slowest')
    n = 100

    for i in range(2):
        t.fd(n*2)
        t.lt(90)
        t.fd(n)
        t.lt(90)

    t.fd(n)
    t.lt(45)

    for i in range(4):
        t.fd(math.sqrt(n**2 +n**2))
        t.lt(90)

    t.lt(45)
    t.fd(n*2)

#CHOCE THE ONE OF THIS
# squer_in()
# squars()
# home()

t.done()