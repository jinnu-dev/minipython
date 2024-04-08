# if~elif / for / while
# if~elif 가위바위보 게임 만들기
import random
hand = input("나의 가위/바위/보 ==> ")
comhand = random.choice(['가위','바위','보'])

if hand == "가위":
    if comhand == "가위" :
        print("나 : {0}  vs 컴퓨터 : {1}\n결과는 비겼습니다.".format(hand, comhand))
    elif comhand == "바위" :
        print("나 : {0}  vs 컴퓨터 : {1}\n결과는 이겼습니다.".format(hand, comhand))
    elif comhand == "보" :
        print("나 : {0}  vs 컴퓨터 : {1}\n결과는 졌습니다.".format(hand, comhand))
elif hand == "바위":
    if comhand == "가위" :
        print("나 : {0}  vs 컴퓨터 : {1}\n결과는 졌습니다.".format(hand, comhand))
    elif comhand == "바위" :
        print("나 : {0}  vs 컴퓨터 : {1}\n결과는 비겼습니다.".format(hand, comhand))
    elif comhand == "보" :
        print("나 : {0}  vs 컴퓨터 : {1}\n결과는 이겼습니다.".format(hand, comhand))
elif hand == "보":
    if comhand == "가위" :
        print("나 : {0}  vs 컴퓨터 : {1}\n결과는 졌습니다.".format(hand, comhand))
    elif comhand == "바위" :
        print("나 : {0}  vs 컴퓨터 : {1}\n결과는 이겼습니다.".format(hand, comhand))
    elif comhand == "보" :
        print("나 : {0}  vs 컴퓨터 : {1}\n결과는 비겼습니다.".format(hand, comhand))

    
# 리스트 딕셔너리 튜플


# 함수 호출