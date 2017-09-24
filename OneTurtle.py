# Turtle-gram tests
# March 2017
# ImageTools functions adapted from Susan Fox, Macalester College Computer Science
# Written by Richard Graham

import turtle
from imageTools import *
from imageToolsTools import *


# GLOBALS #

pic = makePicture("flower.png")

w = getWidth(pic)
h = getHeight(pic)

sc = turtle.Screen()
sc.setup(width=w, height=h)

# SPEED #
sc.tracer(2048)

# DRAWING #
tu = turtle.Turtle()

colordict = {
    'violet red': (247, 83, 148), 'carnation pink': (255, 170, 204), 'gray': (149, 145, 140),
    'blue violet': (115, 102, 189), 'white': (237, 237, 237), 'cerulean': (29, 172, 214), 'violet': (146, 110, 174),
    'red': (238, 32, 77), 'green': (28, 172, 120), 'indigo': (93, 118, 203), 'yellow green': (197, 227, 132),
    'orange': (255, 117, 56), 'green yellow': (240, 232, 145), 'black': (35, 35, 35), 'red orange': (255, 83, 73),
    'red violet': (192, 68, 143), 'dandelion': (253, 219, 109), 'brown': (180, 103, 77), 'yellow': (252, 232, 131),
    'blue': (31, 117, 254), 'scarlet': (252, 40, 71), 'yellow orange': (255, 182, 83), 'blue green': (25, 158, 189),
    'apricot': (253, 217, 181)
}

def closest_color(palette, inpic):
    for y in range(h):
        for x in range(w):
            pix = getPixel(inpic, x, y)
            r, g, b = getRGB(pix)
            for rgb in palette.values():
                pass