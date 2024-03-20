inmoney = int(input("투입한 돈: "))
price = int(input("물건값: "))
outmoney = inmoney-price
print("거스름돈:", outmoney)
print("500원 동전의 개수: ", outmoney//500)
print("100 동전의 개수: ", (outmoney%500)//100)
print("10 동전의 개수: ", ((outmoney%500)%100)//10)
