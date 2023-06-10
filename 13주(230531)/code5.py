#함수5
import turtle
t=turtle.Turtle()
t.shape("turtle")

def sqr(x,y,length,color):
    t.color(color)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    for i in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()


sqr(-200,0,100,"blue")
sqr(0,0,100,"red")
sqr(200,0,100,"green")

turtle.done()
