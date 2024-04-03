# 5주차
# if 조건식 : 
#     실행할문장

# 짝홀 판별
num = int(input("숫자를 입력 ==> "))

if num % 2 == 0 :
    print("짝수입니다.")
else : 
    print("홀수입니다.")


# 100보다작다, 100에서 1000사이다, 1000보다 크다
if num < 100:
    print("100보다 작다.")
else :
    if num < 1000 :
        print("100에서 1000사이다.")
    else :
        print("1000보다 크다.")

# 성적출력
if num >= 90 :
    print("A", end=' ')
else :
    if num >= 80 :
        print("B", end=' ')
    else : 
        if num >= 70 :
            print("C", end=' ')
        else :
            if num >= 60 :
                print("D", end=' ')
            else :
                print("F", end=' ')

print("학점입니다.")

