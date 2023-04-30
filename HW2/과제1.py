#복리 이자율
i=0
money=1000
while True:
    i=i+1
    money+=money*0.09
    print("%d 년후 %f가 되었습니다."%(i,money))
    if money>=2000:
        break
    
print("")
print("")
print("%d 년이 걸립니다."% i)

