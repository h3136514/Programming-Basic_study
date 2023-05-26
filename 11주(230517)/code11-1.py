myT=(10,30,50)
myL=list(myT)       #튜플을 리스트(값 변경및 추가 가능)로 바꿈
myL.append(100)
myT=tuple(myL)      #리스트를 튜플로 바꿈

print(myT)
