import random
import turtle
window = turtle.Screen()
window.colormode(255)
window.setup(1000, 1000)

def koch_curve(t, depth, size):
    if (depth == 1):
        t.fd(size)
        t.color(random.randrange(255), random.randrange(255), random.randrange(255))
    else:
        koch_curve(t, depth-1, size - 1)
        t.lt(60)
        koch_curve(t, depth-1, size - 1)
        t.rt(120)
        koch_curve(t, depth-1, size - 1)
        t.lt(60)
        koch_curve(t, depth-1, size - 1)
        t.rt(90)

def righttri(t, size):
    t.lt(90)
    t.fd(size*(3**.5))
    t.rt(150)
    t.fd(size*2)
    t.right(120)
    t.fd(size)
    t.rt(180)

def sierpinski(t, depth, size):
    if depth == 1:
        t.color(255,70,250)
        righttri(t, size)
        t.color(70,230,255)
    else:
        sierpinski(t, depth-1, size/2)
        t.fd(size/2)
        sierpinski(t, depth-1, size/2)
        t.bk(size/2)
        t.lt(90)
        t.fd((size*(3**.5))/2)
        t.rt(90)
        sierpinski(t, depth-1, size/2)
        t.rt(90)
        t.fd((size * (3**.5)/2))
        t.lt(90)

def tree(t, depth, size, angle):
    t.width(3)
    if depth == 0:
        angel = (random.randrange(130))
        t.width(5)
        t.fd(size)
        t.color(223, 82,134)
        t.fd(size)
        t.bk(size)
        t.rt(angel)
        t.color(255, 192, 203)
        t.fd(size)
        t.bk(size)
        t.lt(angel*2)
        t.fd(size)
        t.bk(size)
        t.rt(angel)
        t.color("brown")
        t.width(3)
        t.bk(size)
    else:
        angle += (random.randrange(10))
        size-=(random.randrange(3))
        t.color("brown")
        t.fd(size)
        t.rt(angle)
        tree(t, depth-1, size - 6, angle)
        t.lt(2 * angle)
        tree(t, depth-1, size - 6, angle)

window.exitonclick
