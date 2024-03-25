# 기말 평균 학점 구하기 
python = 3
mobile = 2
execl = 1
B = 3.5
A0 = 4
A = 4.5
avg = (python*B) + (mobile*A0) + (execl*A) / (python + mobile + execl)
print("평균 학점 :",avg)

# 오늘의 퇴근 문제 
Kor = int(input("국어 점수 :")) #Kor는 국어
Eng = int(input("영어 점수 :")) #Eng는 영어
Mat = int(input("수학 점수 :")) #Mat는 수학
avg = Kor + Eng + Mat / 3
print("평균 점수 :", avg)

#2장 3장 도전문제 
Name = input("이름을 입력하시오:")
print(Name, "씨 안녕하세요? ")
print("파이썬에 오신 것을 환영합니다.")
n1 = int(input("첫 번째 정수를 입력하세요:"))
n2 = int(input("두 번째 정수를 입력하세요:"))
print(n1,"과",n2,"의 합은",n1+n2,"입니다.")

#2장 3장 도전문제
m = int(input("투입한 돈:")) #투입한 돈
m1 = int(input("물건값:"))  #물건값
Ch = m - m1 #거스름돈
print("500원 동전의 개수:",Ch//500)
print("100원 동전의 개수:",(Ch%500)//100)