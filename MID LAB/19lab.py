from graphics import *


def main():
    win = GraphWin("cse 342", 500, 500)
    win.setBackground(color_rgb(0, 100, 0))
    pt1 = Point(200, 200)
    cir = Circle(pt1, 80)
    cir.setWidth(5)
    cir.setOutline(color_rgb(255, 0, 0))
    cir.setFill(color_rgb(255, 0, 0))
    cir.draw(win)

    ln = Line(Point(120, 200), Point(280, 200))
    ln.setWidth(5)
    ln.setOutline(color_rgb(180, 150, 260))
    ln.setFill(color_rgb(155, 0, 0))
    ln.draw(win)

    ln = Line(Point(200, 120), Point(200, 280))
    ln.setWidth(5)
    ln.setOutline(color_rgb(180, 150, 260))
    ln.setFill(color_rgb(155, 0, 0))
    ln.draw(win)

    tri=Polygon(Point(300, 300),Point(400, 400), Point(300,400))
    tri.setWidth(5)
    tri.setOutline(color_rgb(100, 150, 200))
    tri.setFill(color_rgb(0, 0, 0))
    tri.draw(win)

    text=Text(Point(150,50), "Jovan Ifte Aminul")
    text.draw(win)




    win.getMouse()
    win.close()


main()
