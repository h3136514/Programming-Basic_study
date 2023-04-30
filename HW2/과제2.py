#(turtle) 반복문으로 별 그리기
import turtle
t=turtle.Turtle()
t.shape('turtle')
t.pencolor("blue")         #펜색깔
turtle.bgcolor("pink")      #배경 색깔
for i in range(5):
    t.forward(200)
    t.right(144)
   


turtle.done()