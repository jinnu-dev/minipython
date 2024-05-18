# after() 명령 사용하기
import tkinter
tmr = 0 #type : int
def count_up():
    global tmr
    tmr = tmr + 1
    label["text"] = tmr
    root.after (1000, count_up)

root = tkinter.Tk()
label = tkinter.Label(font=("Times new Roman", 80))
label.pack()
root.after(1000, count_up)
root.mainloop()