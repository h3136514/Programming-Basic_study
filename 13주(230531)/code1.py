#함수(global 변수)
def cal_area(radius):
    global result
    result=3.14*radius**2
    return

result=0

r=float(input("원의 반지름 : "))
cal_area(r)
print(result)
