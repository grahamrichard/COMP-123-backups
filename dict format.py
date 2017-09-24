colordict = {

    "red": [238, 32, 77], "yellow": [252, 232, 131], "blue": [31, 117, 254], "brown": [180, 103, 77],
    "orange": [255, 117, 56], "green": [28, 172, 120], "violet": [146, 110, 174], "black": [35, 35, 35],
    "carnation pink": [255, 170, 204], "yellow orange": [255, 182, 83], "blue green": [25, 158, 189],
    "red violet": [192, 68, 143], "red orange": [255, 83, 73], "yellow green": [197, 227, 132],
    "blue violet": [115, 102, 189], "white": [237, 237, 237], "violet red": [247, 83, 148],
    "dandelion": [253, 219, 109], "cerulean": [29, 172, 214], "apricot": [253, 217, 181], "scarlet": [252, 40, 71],
    "green yellow": [240, 232, 145], "indigo": [93, 118, 203], "gray": [149, 145, 140]
}

tupledict = {
    'violet red': (247, 83, 148), 'carnation pink': (255, 170, 204), 'gray': (149, 145, 140),
    'blue violet': (115, 102, 189), 'white': (237, 237, 237), 'cerulean': (29, 172, 214), 'violet': (146, 110, 174),
    'red': (238, 32, 77), 'green': (28, 172, 120), 'indigo': (93, 118, 203), 'yellow green': (197, 227, 132),
    'orange': (255, 117, 56), 'green yellow': (240, 232, 145), 'black': (35, 35, 35), 'red orange': (255, 83, 73),
    'red violet': (192, 68, 143), 'dandelion': (253, 219, 109), 'brown': (180, 103, 77), 'yellow': (252, 232, 131),
    'blue': (31, 117, 254), 'scarlet': (252, 40, 71), 'yellow orange': (255, 182, 83), 'blue green': (25, 158, 189),
    'apricot': (253, 217, 181)
}


newdict = {}

for key in colordict.keys():
    tmp = colordict[key]
    tmp1 = tmp[0]
    tmp2 = tmp[1]
    tmp3 = tmp[2]
    newval = (tmp1, tmp2, tmp3)
    newdict[key] = newval

print(newdict)

