#break 제어문 사용
a,b=0,0
hap=0
while True:
    print("0을 입력하면 종료합니다.")
    a=int(input("첫번 째 숫자 : "))
    if a==0:
        break
    b=int(input("두번 째 숫자 : "))
    if b==0:
        break
    hap=a+b
    print("%d+%d=%d"%(a,b,hap)) 
print("0을 입력하여 종료합니다.")
