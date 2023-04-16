money, c500, c100, c40, c10 = 0,0,0,0,0

money=int(input("교환할 금액을 적으세요: "))

c500 =money//500    #소수점이 안나오게 나눠야되므로
money %=500

c100 =money//100
money %=100

c50 =money//50
money %=50

c10 =money//10
money %=10

print("500원 동전  => %d개" % c500)

print("100원 동전  =>  %d개" % c100)

print("50원 동전  =>  %d개" % c50)

print("10원 동전  =>  %d개" % c10)

print("교환하지 못한 돈  =>  %d원 " % money)
