#random 주사위
import random
#A,B각각 주사위를 두번 던짐
A1=random.randrange(1,7)
A2=random.randrange(1,7)
B1=random.randrange(1,7)
B2=random.randrange(1,7)
#A,B의 두주사위의 합
A=A1+A2
B=B1+B2

print("A의 주사위 숫자는 "+str(A1)+" "+str(A2)+"입니다.")
print("B의 주사위 숫자는 "+str(B1)+" "+str(B2)+"입니다.")

#A,B주사위의 합 비교
if(A>B):
    print("A가 이겼습니다.")
elif(A<B):
    print("A가 이겼습니다.")
else:
    print("둘이 비겼네요.")
