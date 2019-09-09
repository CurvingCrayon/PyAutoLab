# Code by Hayden Keers (September 2019)
import tkinter
import xml.etree.ElementTree as XML
def render(master, element, num, direction):
    # master must always be a tkinter object
    # element must always be an elementtree object
    # num is the default positioning number
    # direction determines what the direction means: 0 = nothing, 1 = vertical, 2 = horizontal, 3 = both
    # direction and num are superseded by explicitly set xml values
    if element.get("text"):
        tkElem = getattr(tkinter, element.tag.capitalize())(master, text = element.get("text"))
    else:
        tkElem = getattr(tkinter, element.tag.capitalize())(master)
    if direction == 1 or direction == 3:
        newRow = getRow(element, num)
    else: 
        newRow = getRow(element, 0)
    if direction == 2 or direction == 3:
        newCol = getCol(element, num)
    else: 
        newCol = getCol(element, 0)
    tkElem.grid(row = newRow, column = newCol)
    elemNum = 0
    newDir = getDir(element, 0)
    for subelement in element:
        render(tkElem, subelement, elemNum, newDir)
        elemNum += 1
    return tkElem

#TODO: attributes

def getAttr(element, val):
    for attr in element.attrib:
        if attr == val:
            return element.get(attr)
    return 0

def getRow(element, num):
    txt = getAttr(element, "row")
    if txt != 0 and txt.isdigit():
        return int(txt)
    return num

def getCol(element, num):
    txt = getAttr(element, "column")
    if txt != 0 and txt.isdigit():
        return int(txt)
    return num

def getDir(element, num):
    txt = getAttr(element, "dir")
    if txt != 0 and txt.isdigit():
        return int(txt)
    return num