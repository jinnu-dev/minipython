# 실시간 키 입력받기
import tkinter

# key= 0
# def key_down(e):
#     global key
#     key = e.keycode

# def main_proc():
#     label["text"] = key
#     root.after(1000, main_proc)

# root = tkinter.Tk()
# root.title("실시간 키 입력")
# root.bind("<KeyPress>",key_down)
# label = tkinter.Label(font=("Times New Roman", 80))
# label.pack()
# main_proc()
# root.mainloop()

# 실시간 방향키로 캐릭터 움직이기
key = ""
def key_down(e):
    global key
    key = e.keysym

def key_up(e):
    global key
    key = ""

cx = 400
cy = 300

def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    canvas.coords("MYCHR", cx, cy)
    root.after(100, main_proc)

root = tkinter.Tk()
root.title("캐릭터이동")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width = 800, height = 600, bg="lightgreen")
canvas.pack()
img = tkinter.PhotoImage(file="mimi.png")
canvas.create_image(cx,cy,image=img, tag="MYCHR")
main_proc()
root.mainloop()

    