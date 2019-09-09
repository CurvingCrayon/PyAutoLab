import tkinter as tk
def lbl(win, txt):
    w = tk.Frame(win)
    lb = tk.Label(w,text = txt).grid(row = 0, column = 0)
    tf = tk.Entry(w).grid(row = 0, column = 1)
    return w