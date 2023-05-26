#재고 관리
items={"음료":10, "펜":5, "휴지":20, "책":5, "사과":13}

while True:
    print("---------------현재의 재고의 상태---------------")
    print(items)
    print("***********************")
    print("0. 종료")
    print("1. 재고 추가")
    print("2. 재고 삭제")
    print("***********************")
    word=int(input("무엇을 하시겠습니까?: "))
    if word ==1:
        item=input("추가할 상품의 이름을 입력해주세요 : ")
        item_value=int(input("재고의 갯수를 입력해주세요 : "))
        items[item]=item_value
    elif word ==2:
        item=input("삭제할 상품의 이름을 입력해주세요 : ")
        del(items[item])
    elif word ==0:
        break




