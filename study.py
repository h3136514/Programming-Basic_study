#한글과 영문자들만 남겨주기(250p,11번)

str1=input("글을 입력하세요:")
str2=''
strlen=len(str1)
for i in range(0,strlen):
    if str1[i].isalpha():
         str2 +=str1[i]

print(str2)

#함수(전역변수)
'''
def func1():
    global a
    a= 10
    print("func1()에서 a의 값은:%d" % a)

    
def func2():
    print("func2()에서 a의 값은:%d" % a)



a=20

func1() 
func2()
'''
'''
def func1(v1,v2,v3=0):
    a=v1
    b=v2
    lista=[]
    lista.append(a)
    lista.append(b)
    return a,b


c=[]
c=list(func1(10,20))
print(c)
''' 
#함수 여러개의 반환값 
def func1(v1):
    v1[0]=100
    return 10, 'ada', 20


a=[10,20]
b=func1(a) #함수의 기본 여러 반환값은 튜플
print(a)    #리스트는 참조에 의한 전달(메모리 공간이 공유되는 방식) =>a[0]값 수정
print(b)

