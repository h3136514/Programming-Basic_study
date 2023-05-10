import turtle
t=turtle.Turtle()
t.shape("turtle")

color_list=[]
for i in range(5):
    color_list.append(input("색상 #%d을  입력하시오: "%i))

for i in range(5):
    t.fillcolor(color_list[i])
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.fd(100)

