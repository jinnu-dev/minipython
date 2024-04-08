import random
myHand = input("나의 가위/바위/보 ==>")
comHand = random.choice(["가위", "바위", "보"])
print("컴퓨터의 가위/바위/보 ==>", comHand)

if myHand == "가위" : 
    if comHand == "가위" : 
        print("비겼습니다.")
    elif comHand == "바위" :
        print("졌습니다.")
    elif comHand == "보" :
        print("이겼습니다.")
elif myHand == "바위" :
    if comHand == "가위" : 
        print("이겼습니다.")
    elif comHand == "바위" :
        print("비겼습니다.")
    elif comHand == "보" :
        print("졌습니다.")
elif myHand == "보" :
    if comHand == "가위" : 
        print("졌습니다.")
    elif comHand == "바위" :
        print("이겼습니다.")
    elif comHand == "보" :
        print("비겼습니다.")