#일정 애플리케이션
cal={}
while True:
    day=input("날짜를 입력하시오(단, q를 누르면 종료합니다): ")
    if day =='q':
        break
    work=input("일정을 입력하시오: ")
    cal[day]=work

print(cal)
