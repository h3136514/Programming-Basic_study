#(for문)입력한 단을 거꾸로 출력하도록 해보세요
dan,i=0,0
dan=int(input("단을 입력하세요: "))
for i in range(9,0,-1):     #9에서 시작해서 1까지 -1씩 감소
    print("%d x %d = %2d"%(i, dan, i*dan)) #주의 형식지정자가 여러개 있을때 "%" 뒤에는 괄호를 묶어서 표시해야됨, 2d==>자리수 지정,