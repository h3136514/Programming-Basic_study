#별
#case 1
a=5
for i in range(1,a+1):
    print("*"*i) #i의 값으로 별 출력
"""
i,j=0,0

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
"""       
print("-------------------------")
#case 2
for i in range(1,a+1):
    print("*"*(a-i+1)) 
print("-------------------------")

#case 3(빈문자 +별)
for i in range(1,a+1):
     print(" "*(a-i)+"*"*i)
print("-------------------------")

#case 4
for i in range(1,a+1):
    print(" "*(i-1) + "*"*(a-i+1))
print("-------------------------")

#case5(수열, 별=i*2 -1개 )
for i in range(1,a+1):
    print(" "*(a-i) + "*"*(2*i-1))
print("-------------------------")

#case6(2개 합침 3,4)
for i in range(1,a+1):
    print(" "*(a-i) +"*"*i )
for i in range(1,a+1):
    print(" "*i +"*"*(a-i) )
print("-------------------------")

#case7(트리2개 5번 2개)
for i in range(1,a+1):
    print(" "*(a-i)+"*"*(2*i-1))
for i in range(1,a+1):
    print(" "*i+"*"*(2*(a-i)-1))
print("-------------------------")