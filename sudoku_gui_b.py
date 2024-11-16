import tkinter as tk
import tkinter.font as fnt

from tkinter import *
win = tk.Tk()  # Application Name
win.geometry("400x400")
win.title("Sudoku GUI App")  # Label
frame1 = tk.Frame(win, width=300, height=400, bg="#3d6466")
frame1.grid(row=0, column=0)

rows = []

for i in range(9):

    cols = []

    for j in range(9):

        #e = Entry(relief=GROOVE, width=1, font=fnt.Font(size=20))
        e = Entry(frame1, width=2, font=fnt.Font(size=20))

        e.grid(row=i, column=j, sticky=NSEW)

        e.insert(END, 0)

        cols.append(e)

    rows.append(cols)



mainloop()