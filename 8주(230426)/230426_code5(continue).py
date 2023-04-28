#continue 제어문 
hap,i=0,0

for i in range(1,101): 
    if i %3==0:
        continue
    hap +=i
print("1-100 중 3의 배수를 제외한 합은 %d이다."%hap)
