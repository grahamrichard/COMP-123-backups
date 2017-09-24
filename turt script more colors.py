# Turtle-gram tests
# March 2017
# ImageTools functions adapted from Susan Fox, Macalester College Computer Science
# Written by Richard Graham

import turtle
from imageToolsTools import *

pic = makePicture("yike.jpg")
# show(pic)

w = getWidth(pic)
h = getHeight(pic)

sc = turtle.Screen()
sc.setup(width=w, height=h)
sc.tracer(2048)

colordict = {

    "red": [238, 32, 77], "yellow": [252, 232, 131], "blue": [31, 117, 254], "brown": [180, 103, 77],
    "orange": [255, 117, 56], "green": [28, 172, 120], "violet": [146, 110, 174], "black": [35, 35, 35],
    "carnation pink": [255, 170, 204], "yellow orange": [255, 182, 83], "blue green": [25, 158, 189],
    "red violet": [192, 68, 143], "red orange": [255, 83, 73], "yellow green": [197, 227, 132],
    "blue violet": [115, 102, 189], "white": [237, 237, 237], "violet red": [247, 83, 148],
    "dandelion": [253, 219, 109], "cerulean": [29, 172, 214], "apricot": [253, 217, 181], "scarlet": [252, 40, 71],
    "green yellow": [240, 232, 145], "indigo": [93, 118, 203], "gray": [149, 145, 140]
}

palette = [

    'blue violet', 'violet', 'orange', 'brown', 'blue', 'yellow', 'apricot', 'white', 'red orange', 'cerulean',
    'gray', 'blue green', 'black', 'indigo', 'scarlet', 'red', 'green', 'yellow green', 'green yellow',
    'dandelion', 'carnation pink', 'violet red', 'red violet', 'yellow orange'
]

sequence = {
    0: 'green yellow', 1: 'blue violet', 2: 'yellow', 3: 'gray', 4: 'dandelion', 5: 'carnation pink', 6: 'apricot', 7:
    'blue green', 8: 'brown', 9: 'indigo', 10: 'violet red', 11: 'red violet', 12: 'scarlet', 13: 'orange', 14:
    'black', 15: 'white', 16: 'yellow green', 17: 'red', 18: 'cerulean', 19: 'red orange', 20: 'yellow orange',
    21: 'blue', 22: 'green', 23: 'violet'
}

turtlist = []


# FIXME: this one's wrong
# def maketurtles(palette, turtles):
#     accumulator = 1
#     for i in range(len(palette)):
#         tempname = palette[accumulator]
#         turtles.append(tempname.turtle.Turtle())
#         accumulator += 1
#     return turtles



# maketurtles(colorlist, colordict)

print(turtlist)



# def makelists(palette):
#     for col in palette.keys():
#         listname = "FIXME"


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


# pixel_params(pic, rpoints, gpoints, bpoints)
# turtleprint(tr, tg, tb, rpoints, gpoints, bpoints)
#
# sc.exitonclick()
