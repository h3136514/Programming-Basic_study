#가장큰 숫자 판별(elif문 사용)
num1= int(input("첫 번째 숫자를 입력하시오: "))
num2= int(input("두 번째 숫자를 입력하시오: "))
num3= int(input("세 번째 숫자를 입력하시오: "))

if(num1>num2)and(num1>num3):
    print("가장 큰 숫자는  "+str(num1)+"입니다")
elif(num2>num1)and(num2>num3):
    print("가장 큰 숫자는  "+str(num2)+"입니다")
else:
    print("가장 큰 숫자는  "+str(num3)+"입니다")
