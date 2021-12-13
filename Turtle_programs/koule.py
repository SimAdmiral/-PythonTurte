import turtle as t
pocet = int(input('set a count of balls '))
t.pu()
t.goto(-t.Screen().window_width()//2 +  20, 0)
p = pocet
pocet1 = 0
x = 0
fd = int(input('set the lenth of side'))
gule = 0
ano = True
a = 0

t.speed(0)
t.Screen().setup(startx= 750, starty= 0)

while True:
    while ano:
        a = 0
        x = 1
        while not ( 0 >= pocet):
            a += 1
            pocet -= x
            x += 1
        ano = False

    for i in range(a):
        t.pd()
        t.color('black', 'yellow')
        t.begin_fill()
        t.circle(fd)
        t.end_fill()
        t.pu()
        t.fd(fd*2)
        gule += 1

        if gule >= p:
            t.done()

    t.backward(fd*2)

    for i in range(a-1):
        t.backward(fd*2)
    t.fd(fd)
    t.lt(90)
    t.fd(fd*2 - fd//4)
    t.rt(90)
    a -= 1

t.done()


# x = 1
# def checking(pocet, x):
#     if pocet + x == pocet + 1:
#         global a
#         pass
#     #global x
#     #x = 1
#     while not ( 0 >= pocet):
#         a += 1
#         pocet -= x
#         x += 1
