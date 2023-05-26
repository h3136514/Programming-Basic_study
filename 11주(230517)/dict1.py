#한영 사전
kor_dict={}

kor_dict['하나']="one"
kor_dict['둘']="two"
kor_dict['셋']="three"

while True:
    word=input("단어를 입력하세요(단, q를 누르면 종료합니다 ) : ")
    if word =='q':
        break
    print(kor_dict[word])
