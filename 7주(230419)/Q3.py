#(for문) 숫자를 하나 입력받고, 그 숫자가 소수인지를 체크하기
num=int(input("*** 숫자를 입력하세요: "))
ss=True #소수 판별 변수

for i in range(2,num,1):
    if(num%i==0):
        ss=False

if(ss==False):
    print("%d는 소수가 아닙니다."% num)
else:
    print("%d는 소수입니다."% num)

