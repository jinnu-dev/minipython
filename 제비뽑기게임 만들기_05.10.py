import tkinter
import random

#버튼 클릭시 랜덤으로 대길, 중길, 소길 흉 출력
def click_btn():
    label["text"] = random.choice(["대길","중길","소길","흉"])
    label.update()

root = tkinter.Tk()
root.title("제비뽑기 프로그램")
root.resizable(False, False) #윈도우 (가로, 세로) 크기 변경 못하게 하는것
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gasou = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400,300, image=gasou)

# GUI 배치
label = tkinter.Label(root, text = "??", font=("궁서체",120) , bg = "white")
label.place(x=380,y=60)
button = tkinter.Button(root, text="제비뽑기", font=("궁서체",36), fg="green", command=click_btn)
button.place(x=360, y=400)

root.mainloop()