import tkinter
import xml.etree.ElementTree as XML
import xmlGui as XG
import math
import events
import functions as fx
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
tabs.grid(row    = 1)

XG.render(runTab, XML.ElementTree(file = "layout/runTab.xml").getroot(), 0, 1).grid(row = 0)

c = tkinter.Canvas(win, bg = "white")
c.grid(row = 2)    
events.setCanvas(c)

win.mainloop()
