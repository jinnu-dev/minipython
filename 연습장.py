import tkinter
import random

def click_btn():
    label["text"] = random.choice(["대길","중길","소길","흉"])
    label.update()

root = tkinter.Tk()
root.title = "제비뽑기 게임"
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600 )
canvas.pack()
gasou = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400,300, image=gasou)

label = tkinter.Label(root, text = "??", font=("궁서체", 120), bg = "black", fg="white")
label.place(x=380, y=60)
button = tkinter.Button(root, text = "제비뽑기", font = ("궁서체", 60), fg="green", command=click_btn)
button.place(x=360, y=400)


root.mainloop()