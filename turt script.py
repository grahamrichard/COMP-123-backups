# Turtle-gram tests
# Feb 2017
# ImageTools functions adapted from Susan Fox, Macalester College Computer Science
# Written by Richard Graham

import turtle
from imageToolsTools import *
# class TurtleTrace:
#     """an instance of this class will recreate the image parameter supplied at initialization with 3 primary-colored
#     turtles. this process will take a very long time and will result in poor image quality. please be patient."""
#     def __init__(self, image):
#         """image parameter must be an absolute file path as a string"""
#         print("tracing image")
#         self.pic = makePicture(image)
#         self.sc = turtle.Screen()
#         self.sc.exitonclick()
#
#         self.w = getWidth(self.pic)
#         self.h = getHeight(self.pic)
#         self.sc.setup(width=self.w, height=self.h)
#
#         self.tr = turtle.Turtle()
#         self.tg = turtle.Turtle()
#         self.tb = turtle.Turtle()
#
#         self.tlist = [self.tr, self.tg, self.tb]
#         self.rpoints = []
#         self.gpoints = []
#         self.bpoints = []
#         self.operations = {self.tr: self.rpoints, self.tg: self.gpoints, self.tb: self.bpoints}
#
#     def prep(self):
#         for turt in self.tlist:
#             turt.penup()
#             turt.goto(0, 0)
#
#     def analyze_image(self):
#         for y in range(self.h):
#             for x in range(self.w):
#                 pix = getPixel(self.pic, x, y)
#                 r, g, b = getRGB(pix)
#                 if r > g and r > b:
#                     self.rpoints.append([x, y])
#                 elif g >= r and g >= b:
#                     self.gpoints.append([x, y])
#                 elif b > r and b > g:
#                     self.bpoints.append([x, y])
#
#     def draw(self):
#         for k, v in self.operations.items():
#             for points in v:
#                 k.goto(points)
#                 k.stamp()
#                 k.penup()
#
#     def go(self):
#         self.prep()
#         self.analyze_image()
#         self.draw()
#
#

# def setup(image):
#     """sets up turtle window at size of input image and sets turtles to start.
#     image parameter must be an absolute file path."""

pic = makePicture("flower.png")   # Image must be smaller than native screen resolution for the turtle screen to
# show(pic)                         # display properly.

w = getWidth(pic)
h = getHeight(pic)

sc = turtle.Screen()
sc.setup(width=w, height=h)
sc.tracer(2048)                     # Affects the turtle refresh rate. Larger numbers result in faster drawing, i.e.
                                    # the turtle refreshes every 2048 pixels.
tr = turtle.Turtle()
tr.color("red")
tr.pensize(1)
tr.speed(0)
tr.shape("turtle")

tg = turtle.Turtle()
tg.color("green")
tg.pensize(1)
tg.speed(0)
tg.shape("turtle")

tb = turtle.Turtle()
tb.color("blue")
tb.pensize(1)
tb.speed(0)
tb.shape("turtle")

rpoints = []
gpoints = []
bpoints = []


def pixel_params(image, rlist, glist, blist):
    for y in range(h):
        for x in range(w):
            pix = getPixel(image, x, y)
            r, g, b = getRGB(pix)
            if r > g and r > b:
                rlist.append([x, y])
            elif g >= r and g >= b:
                glist.append([x, y])
            elif b > r and b > g:
                blist.append([x, y])
    return rlist, glist, blist


def turtleprint(rtu, gtu, btu, rlist, glist, blist):
    for elem in rlist:
        rtu.penup()
        rtu.goto(elem)
        rtu.dot(1, "red")

    for elem in glist:
        gtu.penup()
        gtu.goto(elem)
        gtu.dot(1, "green")

    for elem in blist:
        btu.penup()
        btu.goto(elem)
        btu.dot(1, "blue")

# FUNCTION CALLS
pixel_params(pic, rpoints, gpoints, bpoints)
turtleprint(tr, tg, tb, rpoints, gpoints, bpoints)

sc.exitonclick()
