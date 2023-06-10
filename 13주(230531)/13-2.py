#과제
def sum_func(*para):
    result=0
    for num in para:
        result=result+num

    return result

print("매개변수가 2개인 함수를 호출한 결과 ==> %d"%sum_func(10,20))
print("매개변수가 10개인 함수를 호출한 결과 ==> %d"%sum_func(10,10,10,10,10,10,10,10,10,10))
