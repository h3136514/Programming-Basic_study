import random
a=5
for i in range(1,a+1):
    print(" "*(a-i) + "*"*(2*i-1))
for i in range(a-1,0,-1):
    print(" "*(a-i) + "*"*(2*i-1))


a="""야\n
호"""
a
print(a)
num=10
if num is not 100:
    print("ddddddd")

print(r"\ntest입니다%% %d"%num,end="}}")
if num%3 != 0:
    print("ddd / %dddd"%num)

'''
#141p 연습문제6번(챕터5)
lista=[]
for i in range(1,21,1):
    lista.append(random.randrange(1,21))

print("생성된 리스트",lista)
for i in range(1,21):
    for j in range(0,20):
        if lista[j]==i:
            print("숫자는 %d는(은) 뽑혔습니다."%i)
            break;

'''
i=0

for i in range(9,0,-1):
    print("%d X %d = %4d"%(15,i,15*i))


nn=[100,200,300,400,500]
print(nn)
print(nn[4])

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
def func1(v1):
    v1[0]=100
    return 10, 'ada', 20


a=[10,20]
b=func1(a)
print(a)
print(b)
'''
#한글과 영문자들만 남겨주기(250p,11번)

str1=input("글을 입력하세요:")
str2=''
strlen=len(str1)
for i in range(0,strlen):
    if str1[i].isalpha():
         str2 +=str1[i]

print(str2)
'''