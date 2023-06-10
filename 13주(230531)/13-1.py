#과제1

def max_n(v1,v2,v3=-100000):
    max_num=0
    if v1>=v2 and v1>=v3:
        max_num=v1
    elif v2>=v1 and v2>=v3:
         max_num=v2
    else:
         max_num=v3

    return max_num

n1=int(input("정수를 입력하세요: "))
n2=int(input("정수를 입력하세요: "))
n3=int(input("정수를 입력하세요: "))
print("(%d, %d, %d) 중에서 최대값 : %d"%(n1,n2,n3,max_n(n1,n2,n3)))
print("(%d, %d) 중에서 최대값 : %d"%(n1,n2,max_n(n1,n2)))  
