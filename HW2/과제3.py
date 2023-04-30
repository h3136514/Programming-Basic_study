import random
count=0
a= random.randrange(1,101) #1~100사이 랜덤값 지정
print("1부터 100사이의 숫자를 맞추시오:")
while (True):
    count=count+1
    if count <=10:
        num=int(input("숫자를 입력하시오: "))
    else:
        print("시도횟수를 초과하였습니다.")
        print("정답은 %d"%a)
        break
    if  num < a:
        print("낮음!")
    elif num > a:
        print("높음!")
    else:
        print("시도 횟수=%d"%count)
        break
   