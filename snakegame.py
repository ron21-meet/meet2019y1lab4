import turtle
ron = turtle.Turtle()
def up():
    ron.fd(50)

def down():
    ron.backward(50)
    
def left():
    ron.lt(90)
    
def right():
    ron.rt(90)

turtle.onkeypress(up, "w")
turtle.onkeypress(down, "s")
turtle.onkeypress(left, "a")
turtle.onkeypress(right, "d")



turtle.listen()
turtle.done()
