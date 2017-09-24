# Turtle-gram tests
# Feb 2017
# ImageTools functions adapted from Susan Fox, Macalester College Computer Science
# Written by Richard Graham

import turtle
from imageToolsTools import *


class TurtleTrace:
    """an instance of this class will recreate the image parameter supplied at initialization with 3 primary-colored
    turtles. this process will take a very long time and will result in poor image quality. please be patient."""
    def __init__(self, image):
        """image parameter must be an absolute file path as a string"""
        print("tracing image")
        self.pic = makePicture(image)
        self.sc = turtle.Screen()
        self.sc.exitonclick()

        self.w = getWidth(self.pic)
        self.h = getHeight(self.pic)
        self.sc.setup(width=self.w, height=self.h)

        self.tr = turtle.Turtle()
        self.tg = turtle.Turtle()
        self.tb = turtle.Turtle()

        self.tlist = [self.tr, self.tg, self.tb]
        self.rpoints = []
        self.gpoints = []
        self.bpoints = []
        self.operations = {self.tr: self.rpoints, self.tg: self.gpoints, self.tb: self.bpoints}

    def prep(self):
        for turt in self.tlist:
            turt.penup()
            turt.goto(0, 0)

    def analyze_image(self):
        for y in range(self.h):
            for x in range(self.w):
                pix = getPixel(self.pic, x, y)
                r, g, b = getRGB(pix)
                if r > g and r > b:
                    self.rpoints.append([x, y])
                elif g >= r and g >= b:
                    self.gpoints.append([x, y])
                elif b > r and b > g:
                    self.bpoints.append([x, y])

    def draw(self):
        for k, v in self.operations.items():
            for points in v:
                k.goto(points)
                k.stamp()
                k.penup()

    def go(self):
        self.prep()
        self.analyze_image()
        self.draw()


def main():
    foo = TurtleTrace("/Users/richardgraham/Google Drive/4. Code/turtlegram/flower.png")
    foo.go()

main()


# def setup(image):
#     """sets up turtle window at size of input image and sets turtles to start.
#     image parameter must be an absolute file path."""
#
#     pic = makePicture(image)
#     show(pic)
#
#     w = getWidth(pic)
#     h = getHeight(pic)
#
#     sc = turtle.Screen()
#     sc.setup(width=w, height=h, startx=0, starty=h * -1)
#     sc.exitonclick()
#
#     tr = turtle.Turtle()
#     tg = turtle.Turtle()
#     tb = turtle.Turtle()
#
#     tr.penup()
#     tr.goto(0, 0)
#     tg.penup()
#     tg.goto(0, 0)
#     tb.penup()
#     tb.goto(0, 0)
#
#     return pic, sc, tr, tg, tb
#
# def pixel_params(pic):
#
