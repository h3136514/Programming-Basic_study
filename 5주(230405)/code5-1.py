#커피 가게 매출 계산하기
americano_price=2000
caffelatte_price=3500
cappuccino_price=4500

americano_in =int(input("아메리카노 판매 개수: "))
caffelatte_in=int(input("카페라떼 판매 개수: "))
cappuccino_in=int(input("카푸치노 판매 개수: "))

sales=americano_in*americano_price + caffelatte_in*caffelatte_price + cappuccino_in*cappuccino_price
print("오늘의 총 매출은 ",sales," 입니다.")
