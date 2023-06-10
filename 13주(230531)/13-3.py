#과제3
'''
#재귀함수 사용
def fact_func(num):
    if num <=1:
        return num
    else:
        return num*fact_func(num-1)

print(fact_func(4))
'''
#재귀함수 사용하지 않음

def fact_func(num):
    result=1
    for i in range(1,num+1):
        result *=i

    return result
print(fact_func(4))
