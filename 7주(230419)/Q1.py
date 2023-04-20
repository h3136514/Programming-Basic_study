#(for문)0과 100사이에 있는 7의 배수 합계를 구하시오 
hap=0
for i in range(0,101,7):
    hap=hap+i
print("0과 100사이에 있는 7의 배수 합계: %d"%(hap))     
