#함수4()

def para_func(*para):   
    result=0
    for num in para:
        result +=num
        
    return result

hap=0

hap=para_func(10,20)
print("결과1: %d"% hap)
hap=para_func(10,20,30)
print("결과2: %d"% hap)
hap=para_func(10,20,30,40)
print("결과3: %d"% hap)
