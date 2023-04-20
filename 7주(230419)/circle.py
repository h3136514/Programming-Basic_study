#(turtle) 6개원 그리기 
import turtle
t=turtle.Turtle()
t.width(3)          #펜두께 
t.pencolor("white")         #펜색깔
turtle.bgcolor("navy")      #배경 색깔
for i in range(6):
    t.circle(70)            #거북이가 반지름 70인 원을 돌림
    t.left(60)              #거북이가 왼쪽으로 60도 돌림


turtle.done()
