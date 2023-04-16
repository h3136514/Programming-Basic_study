#거북이(turtle) 동전이미지추가
import random
import turtle

screen=turtle.Screen()

image1="front.gif"
image2="back.gif"

screen.addshape(image1) #이미지를 등록한다
screen.addshape(image2)

t1=turtle.Turtle()
coin=random.randrange(2)
if coin ==0:
    t1.shape(image1) #t1에 image1를 생성한다.
    t1.stamp() #이미지의 좌표설정
else:
    t1.shape(image2)
    t1.stamp() #이미지의 좌표설정
    

