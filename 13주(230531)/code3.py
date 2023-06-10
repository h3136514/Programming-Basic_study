#함수3()

'''
def para2_func(v1,v2):      #def para2_func(v1,v2,v3=0):  ==>2개의 매개변수를 입력해도 오류X
    result=0
    result=v1+v2
    return result

def para3_func(v1,v2,v3):
    result=0
    result=v1+v2+v3
    return result

hap=0
hap=para2_func(10,20) #3개의 매개변수를 입력할경우 오류
print("매개변수가 2개인 경우 : %d"%hap)
hap=para3_func(10,20,30)
print("매개변수가 3개인 경우 : %d"%hap)

'''

def greet(name, msg="입니다"):
    print("hi~",name+","+msg)

greet("홍길동")
