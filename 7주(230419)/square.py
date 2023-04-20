#(turtle)입력한 다각형 그리기
import turtle
t=turtle.Turtle()

s=turtle.textinput("","몇각형을 그릴까요? 숫자로 입력하세요")
n=int(s)        #s(문자열)을 int형으로 변환

for i in range(n):
    t.forward(100)
    t.left(360/n)   #360도에서 나눠야지 내가 웒하는 그림이 나오므로

turtle.done()
