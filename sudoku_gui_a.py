import tkinter as tk
import tkinter.font as fnt

win = tk.Tk()  # Application Name
win.geometry("800x800")
win.title("Sudoku GUI App")  # Label
frame1 = tk.Frame(win, width=500, height=600, bg="#3d6466")
frame1.grid(row=0, column=0)


def click():
    button01 = tk.Button(frame1, text="ouch", command=click).grid(column=20, row=12)
    a = [[() for j in range(9)] for i in range(9)]

    for n in range(4):
        a[n][0] = int(e[n][0].get())
        a[n][0] += n
        e[n][0].set(str(a[n][0]))


def click2():
    n = e[0][0].get()
    print(n)


e = [[(tk.IntVar()) for j in range(9)] for i in range(9)]

entry00 = tk.Entry(frame1, width=1, textvariable=e[0][0], font = fnt.Font(size = 20)).grid(column=0, row=0)
entry10 = tk.Entry(frame1, width=1, textvariable=e[1][0], font = fnt.Font(size = 20)).grid(column=1, row=0)
entry20 = tk.Entry(frame1, width=1, textvariable=e[2][0], font = fnt.Font(size = 20)).grid(column=2, row=0)
entry40 = tk.Entry(frame1, width=1, textvariable=e[3][0], font = fnt.Font(size = 20)).grid(column=3, row=0)
entry50 = tk.Entry(frame1, width=1, textvariable=e[4][0], font = fnt.Font(size = 20)).grid(column=4, row=0)
entry60 = tk.Entry(frame1, width=1, textvariable=e[5][0], font = fnt.Font(size = 20)).grid(column=5, row=0)
entry70 = tk.Entry(frame1, width=1, textvariable=e[6][0], font = fnt.Font(size = 20)).grid(column=6, row=0)
entry80 = tk.Entry(frame1, width=1, textvariable=e[7][0], font = fnt.Font(size = 20)).grid(column=7, row=0)
entry01 = tk.Entry(frame1, width=1, textvariable=e[0][1], font = fnt.Font(size = 20)).grid(column=0, row=1)
entry11 = tk.Entry(frame1, width=1, textvariable=e[1][1], font = fnt.Font(size = 20)).grid(column=1, row=1)
entry21 = tk.Entry(frame1, width=1, textvariable=e[2][1], font = fnt.Font(size = 20)).grid(column=2, row=1)
entry41 = tk.Entry(frame1, width=1, textvariable=e[3][1], font = fnt.Font(size = 20)).grid(column=3, row=1)
entry51 = tk.Entry(frame1, width=1, textvariable=e[4][1], font = fnt.Font(size = 20)).grid(column=4, row=1)
entry61 = tk.Entry(frame1, width=1, textvariable=e[5][1], font = fnt.Font(size = 20)).grid(column=5, row=1)
entry71 = tk.Entry(frame1, width=1, textvariable=e[6][1], font = fnt.Font(size = 20)).grid(column=6, row=1)
entry81 = tk.Entry(frame1, width=1, textvariable=e[7][1], font = fnt.Font(size = 20)).grid(column=7, row=1)
entry02 = tk.Entry(frame1, width=1, textvariable=e[0][2], font = fnt.Font(size = 20)).grid(column=0, row=2)
entry12 = tk.Entry(frame1, width=1, textvariable=e[1][2], font = fnt.Font(size = 20)).grid(column=1, row=2)
entry22 = tk.Entry(frame1, width=1, textvariable=e[2][2], font = fnt.Font(size = 20)).grid(column=2, row=2)
entry42 = tk.Entry(frame1, width=1, textvariable=e[3][2], font = fnt.Font(size = 20)).grid(column=3, row=2)
entry52 = tk.Entry(frame1, width=1, textvariable=e[4][2], font = fnt.Font(size = 20)).grid(column=4, row=2)
entry62 = tk.Entry(frame1, width=1, textvariable=e[5][2], font = fnt.Font(size = 20)).grid(column=5, row=2)
entry72 = tk.Entry(frame1, width=1, textvariable=e[6][2], font = fnt.Font(size = 20)).grid(column=6, row=2)
entry82 = tk.Entry(frame1, width=1, textvariable=e[7][2], font = fnt.Font(size = 20)).grid(column=7, row=2)
entry03 = tk.Entry(frame1, width=1, textvariable=e[0][3], font = fnt.Font(size = 20)).grid(column=0, row=3)
entry13 = tk.Entry(frame1, width=1, textvariable=e[1][3], font = fnt.Font(size = 20)).grid(column=1, row=3)
entry23 = tk.Entry(frame1, width=1, textvariable=e[2][3], font = fnt.Font(size = 20)).grid(column=2, row=3)
entry43 = tk.Entry(frame1, width=1, textvariable=e[3][3], font = fnt.Font(size = 20)).grid(column=3, row=3)
entry53 = tk.Entry(frame1, width=1, textvariable=e[4][3], font = fnt.Font(size = 20)).grid(column=4, row=3)
entry63 = tk.Entry(frame1, width=1, textvariable=e[5][3], font = fnt.Font(size = 20)).grid(column=5, row=3)
entry73 = tk.Entry(frame1, width=1, textvariable=e[6][3], font = fnt.Font(size = 20)).grid(column=6, row=3)
entry83 = tk.Entry(frame1, width=1, textvariable=e[7][3], font = fnt.Font(size = 20)).grid(column=7, row=3)


button01 = tk.Button(frame1, text="submit", command=click2).grid(column=20, row=12)

win.mainloop()
