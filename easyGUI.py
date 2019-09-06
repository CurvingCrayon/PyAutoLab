import tkinter as tk
def lbl(win, txt):
    tk.Label(win,text = txt).grid(row = 0, column = 0)
    tf = tk.Entry(win)
    tf.grid(row = 0, column = 1)