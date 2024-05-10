import tkinter
import tkinter.font
root = tkinter.Tk() #윈도우 요소(객체) 생성
root.title("첫 번째 윈도우") #윈도우 제목 지정
root.geometry("800x600") # 윈도우 크기지정 
# minsize(폭,높이) = 최소크기, maxsize(폭,높이)= 최대크기

#라벨지정
label = tkinter.Label(root, text = "라벨 문자열", font=("궁서체",24))
label.place(x=200, y=100)

#버튼 클릭시 반응하기
def click_btn():
    button["text"] = "클릭했습니다."

#버튼만들기
button = tkinter.Button(root, text="버튼 문자열", font=("Times New Roman", 24), command = click_btn)
button.place(x=200, y=200)




root.mainloop() #윈도우 표시