### 자동 판매기를 시뮬레이션 하는 프로그램을 작성해보자.
## 투입한 돈과 물건값 입력
## 물건값은 100원 단위로 가정
money = int(input("투입한 돈 : "))
values = int(input("물건값 : "))
diff = money - values
print("거스름돈 : ",diff)
print("500원 동전의 개수:",diff//500,"\n100원 동전의 개수: ",(diff%500)/100)

# // 몫 % 나머지