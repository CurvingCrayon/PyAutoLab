import tkinter
import easyGUI as EG
import xml.etree.ElementTree as XML
import xmlGui as XG
from tkinter import ttk
win = tkinter.Tk() 
win.title("PyAutoLab")
#create a title and display it with necessary space
tkinter.Label(win, text = "Hayden's PyAutoLab").grid(row = 0) 
tabs = ttk.Notebook()
#Create main execution tab
runTab = ttk.Frame(tabs)
tabs.add(runTab, text="Run")
#Create setup tab
setupTab = ttk.Frame(tabs)
tabs.add(setupTab, text = "Setup")
#Add tabs
tabs.grid(row = 1)

XG.render(runTab, XML.ElementTree(file = "layout/runTab.xml").getroot(), 0, 1).grid(row = 0)

c = tkinter.Canvas(win)

c.grid(row = 2)
win.mainloop()
