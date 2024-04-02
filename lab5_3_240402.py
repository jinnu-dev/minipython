num = int(input("점수를 입력하시오 ==>"))
if num >= 90 : 
    print("A",end='')
else :
    if num >= 80 :
        print("B", end='')
    else : 
        if num >= 70 : 
            print("C", end='')
        else :
            if num >= 60 :
                print("D", end='')
            else : 
                print("F", end='')
print("학점입니다.")
