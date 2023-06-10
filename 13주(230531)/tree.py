import turtle
#기본 shape는 삼긱형
t=turtle.Turtle()
t.left(90)

def tree(length):
    if length>5:
        t.forward(length)
        t.right(20)
        tree(length-15)
        t.left(40)
        tree(length-15)
        t.right(20)
        t.backward(length)




t.color("green")
t.speed(10)
tree(90)

turtle.done()
