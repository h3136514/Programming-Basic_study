"""
#case1
ss='<<<파<<이>>썬>>>'
ss=ss.replace('<','')
ss=ss.replace('>','')
print(ss)
"""
#case2
instr= "<<<파<<이>>썬>>>"
outstr=""

for i in range(0, len(instr)):
    if instr[i]!='<' and instr[i]!='>':
        outstr+=instr[i]

print("원래 문자열==>"+'[ '+ instr+ ' ]')
print("'<','>' 삭제 문자열==>"+'[ '+ outstr+ ' ]')
