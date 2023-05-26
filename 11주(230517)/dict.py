#사전
eng_dict={}

eng_dict['one']="하나"
eng_dict['two']="둘"
eng_dict['three']="셋"

while True:
    word=input("단어를 입력하세요(단, q를 누르면 종료합니다 ) : ")
    if word =='q':
        break
    print(eng_dict[word])
