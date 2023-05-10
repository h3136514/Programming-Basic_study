aa=[0,0,0,0]
#aa[0]*4        리스트는 합산도 되고 곱셈도 된다.
hap=0

aa[0]=int(input("숫자를 입력하세요 : "))
aa[1]=int(input("숫자를 입력하세요 : "))
aa[2]=int(input("숫자를 입력하세요 : "))
aa[3]=int(input("숫자를 입력하세요 : "))
#코드가 반복 중??
aa.append(50)

hap=aa[0]+aa[1]+aa[2]+aa[3]
print("합 : %d "%hap)
print(aa)
