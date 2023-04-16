#동전던지기
import random

print("동전 던지기 게임")
coin=random.randrange(2) #0,1두개만 쓰겠다 if(1,5)-->1,2,3,4(끝값은 제외함)
if coin == 0:
    print("동전은 앞면입니다")
else:
    print("동전은 뒷면입니다")
