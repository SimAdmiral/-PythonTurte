import turtle
sc = turtle.Screen()
def f():
    turtle.forward(100)
def clear():
    turtle.clear()
sc.onclick(f)
sc.onkey(clear, "Down")
sc.onkey(f, "Up")
sc.listen()
turtle.mainloop()