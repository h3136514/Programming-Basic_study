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

