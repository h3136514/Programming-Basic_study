#거꾸로 문자열 출력
instr, outstr="", ""
count,i=0,0

instr=input("문자열을 입력하세요 : ")

count=len(instr)

for i in range(0, count):
    outstr +=instr[count-(i+1)]

print("거꾸로 출력된 문자열 : %s" % outstr)
