from imageTools import *

def getRange(picture):
    """ Gets a rectangular region by allowing the user to click at two points.
         Returns the x,y coordinates of the first click followed by the second click
         This function's inner workings are complicated and use python tricks that
         I don't really approve of except in crazy circumstances such as this one."""
    show(picture)
    master = picture.dispWindow.master
    ev1 = None
    ev2 = None
    def callback(evt):
        nonlocal ev1, ev2
        if ev1 == None:
            ev1 = evt
            print("Please click to specify bottom right point.")
        else:
            ev2 = evt
            master.quit()
    master.bind("<Button-1>", callback)
    print("Please click to specify upper left point.")
    master.mainloop()
    hide(picture)
    return ev1.x, ev1.y, ev2.x, ev2.y


def getPoint(picture):
    """ gets a point from a picture by showing the picture to the user and having the user click the picture to select a point
        This function's inner workings are complicated and uses python tricks that I don't really approev of except in crazy 
        circumstances such as this one."""
    show(picture)
    master = picture.dispWindow.master
    ev1 = None
    def callback(evt):
        nonlocal ev1
        if ev1 == None:
            ev1 = evt
            master.quit()
    master.bind("<Button-1>", callback)
    print("Please click to specify  point.")
    master.mainloop()
    hide(picture)
    return ev1.x, ev1.y


def wait(picture):
    def callback(evt):
        picture.dispWindow.master.quit()
    picture.dispWindow.master.bind("<Button-1>", callback)
    picture.dispWindow.master.mainloop()
