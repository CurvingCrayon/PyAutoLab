import functions as fx
canvas = 0
def plot(event):
    pts = []
    fx.getPoints(0, 10, "3*x", pts)
    fx.graph(canvas, pts)

def setCanvas(c):
    global canvas
    canvas = c