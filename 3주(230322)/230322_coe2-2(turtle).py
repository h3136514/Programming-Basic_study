import turtle
import random
'''
#직사각형 만들기
turtle.shape('turtle')
turtle.forward(100) #앞으로가기
turtle.right(90)   #각도 돌기
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)

turtle.done() # 끝
'''
#원그리기(색깔채워서)
turtle.shape('turtle')

turtle.fillcolor("blue") #색깔 채우기
turtle.begin_fill()  #시작값
turtle.circle(100)  #원 그리기
turtle.end_fill()   #끝나는 값

turtle.forward(100)

turtle.fillcolor("red") #색깔 채우기
turtle.begin_fill()  #시작값
turtle.circle(200)  #원 그리기
turtle.end_fill()   #끝나는 값


turtle.done()
##함수 선언 부분##
#def screenLeftClick(x,y):
 #   global r,g,b
    
