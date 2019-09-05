import tkinter
from tkinter import ttk
win = tkinter.Tk() 
win.title("PyAutoLab")
#create a title and display it with necessary space
tkinter.Label(win, text = "Hayden's PyAutoLab").pack() 
tabs = ttk.Notebook()
#Create main execution tab
runTab = ttk.Frame(tabs)
tabs.add(runTab, text="Run")
tabs.pack(expand=1, fill="both")
#Create setup tab
setupTab = ttk.Frame(tabs)
tabs.add(setupTab, text = "Setup")
tabs.pack(expand = 1, fill = "both")
win.mainloop()
