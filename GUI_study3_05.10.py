import tkinter
# root = tkinter.Tk()
# root.title("첫번째 텍스트 필드 입력")
# root.geometry("400x200")
# # 입력필드에 get() 을 이용해 문자를 입력하고 버튼을 누르면 그 문자열이 버튼에 표시되게 하기

# def click_btn():
#     txt = entry.get()
#     button["text"] = txt

# entry = tkinter.Entry(width=20)
# entry.place(x=10, y=20)

# button = tkinter.Button(root, text="문자열 얻기", command=click_btn)
# button.place(x=10, y=100)

## 여러행 텍스트 입력 필드
def dlick_btn():
    text.insert(tkinter.END, "몬스터가 나타났다!")

root = tkinter.Tk()
root.title("여러 행 텍스트 입력")
root.geometry("400x200")
button = tkinter.Button(root, text="메세지", command=dlick_btn)
button.pack()
text = tkinter.Text()
text.pack()

root.mainloop()