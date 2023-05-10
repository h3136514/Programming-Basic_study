import turtle
t=turtle.Turtle()
t.shape("turtle")

#리스트 활용 후 색 지정
color_list=["blue", "red","green", "purple"]

for i in range(4):
    t.fillcolor(color_list[i])
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.fd(50)

