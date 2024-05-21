# 8주차 블록낙하게임만들기

# 마우스 입력
import tkinter
neko = [
    [1,0,0,0,0,0,7,7],
    [0,2,0,0,0,0,7,7],
    [0,0,3,0,0,0,0,0],
    [0,0,0,4,0,0,0,0],
    [0,0,0,0,5,0,0,0],
    [0,0,0,0,0,6,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,1,2,3,4,5,6]
]
cursor_X = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

def draw_neko():
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x*72+60, y*72+60, image = img_neko[neko[y][x]])


def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

def mouse_release(e):
    global mouse_c
    mouse_c = 0

def game_main():
    global cursor_X, cursor_y
    if 24 <= mouse_x and mouse_x <24+72*8 and 24 <= mouse_y and mouse_y < 24+72*10 :
        cursor_X = int ((mouse_x - 24) / 72)
        cursor_y = int ((mouse_y - 24) / 72)
    cvs.delete("CURSOR")
    cvs.create_image(cursor_X * 72+60, cursor_y * 72+60, image=cursor, tag="CURSOR")
    # fnt = ("Times New Roman",30)
    # txt = "mouse({},{}){}".format(mouse_x, mouse_y, mouse_c)
    # cvs.delete("TEST")
    # cvs.create_text(456, 384, text = txt, fill = "black", font = fnt, tag="TEST")
    root.after(100, game_main) #실시간 처리 반환

root = tkinter.Tk()
root.title("2차원 리스트 관리")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
root.bind("<ButtonRelease>", mouse_release)
cvs = tkinter.Canvas(root, width = 912, height = 768)
cvs.pack()

bg = tkinter.PhotoImage(file="neko_bg.png")
cursor = tkinter.PhotoImage(file="neko_cursor.png")
cvs.create_image(456,384, image=bg)
img_neko = [
    None,
    tkinter.PhotoImage(file = "neko1.png"),
    tkinter.PhotoImage(file = "neko2.png"),
    tkinter.PhotoImage(file = "neko3.png"),
    tkinter.PhotoImage(file = "neko4.png"),
    tkinter.PhotoImage(file = "neko5.png"),
    tkinter.PhotoImage(file = "neko6.png"),
    tkinter.PhotoImage(file = "neko_niku.png")
]

draw_neko()
# game_main()
root.mainloop()
