import math
def getPoints(start, count, function, points):
    for c in range(count):
        newFunc = function.replace("x", str(c))
        val = eval(newFunc)
        points.append(val)

def graph(canvas, points):
    c = canvas
    for p in range(len(points) - 1):
        # points are offset by 1 to fit on the graph
        canvas.create_line(p + 1, translate(c,points[p]), p + 2, translate(c,points[p+1]))

def translate(canvas, y):
    return canvas.winfo_height() - y
newP = []
getPoints(0, 10, "3*x", newP)
print(newP)
