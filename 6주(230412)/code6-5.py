#거북이(turtle) 사각형,삼각형 그리기
import turtle
t=turtle.Turtle()
t.shape("turtle") #거북이로 모양새를 잡아줌

#데이터를 입력받을 text상자
s=turtle.textinput("도형이름","도형을 입력하세요.")    #textinput(제목,내용)
if s=="사각형":
    s=turtle.numinput("가로길이","가로: ")     #numinput(제목,내용), 문자열로 받음
    w=int(s) #정수형으로 변형
    s=turtle.numinput("세로길이","세로: ")    
    h=int(s)
    t.speed(1) #속도 설정
    t.forward(w) #w(가로)직선그리기
    t.left(90)
    t.forward(h) #h(세로)직선그리기
    t.left(90)
    t.forward(w) #w(가로)직선그리기
    t.left(90)
    t.forward(h) #h(세로)직선그리기
elif s=="삼각형":
    s=turtle.numinput("변길이","변길이: ")
    a=int(s) 
    t.speed(1) #속도 설정
    t.forward(a) #변a 그리기
    t.left(120)
    t.forward(a) #변a 그리기
    t.left(120)
    t.forward(a) #변a 그리기
else:
    pass

turtle.done()
    
