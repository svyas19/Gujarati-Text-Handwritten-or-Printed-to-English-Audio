from PIL import Image
import os

for item in range(1, 68):  # index no of datasets
    os.mkdir('images/' + str(item) + '/' + str(2))
    # Open the image 2.jpg and convert into gray scale
    im = Image.open('images/' + str(item) + '/2.jpg')
    # for resize the image
    im = im.resize((2104, 2896), Image.ANTIALIAS)
    im.save('images/' + str(item) + '/2.jpg', quality=95)
    im = im.convert('LA')  # To convert the image into grey scale
    # calculate the width and height of the image
    [width, height] = im.size

    # number of cols in the image
    col = 11
    # number of rows in the image
    row = 15

    # if the width of the image is x and image has y column then
    # the lenghth of a column = x / y.
    oneWidth = width / col
    # if the height of the image is x and image has y rows then
    # the lenghth of a rows = x / y.
    oneHeight = height / row

    i = 0
    j = 0
    x = 0
    y = 0

    # the original image is very large.
    # it need to be cropped.
    # the function crop require a box to crop the image
    # the box contains [left,top,right,bottom] pixel.
    #   (left,top)
    #     -------------------------------------
    #    |                       |
    #    |                       |
    #    |                       |
    #    |                       |
    #    |                       |
    #    |                       |
    #     ---------------------------------------
    #                            (right,bottom)

    for i in range(1, row + 1):
        for j in range(1, col):
            x = oneWidth * j
            # calculate the next box
            box = (x, y, x + oneWidth, y + oneHeight)
            # crop the original image. Hence getting a 2d mxn array
            cimage = im.crop(box)
            cimage.save('images/' + str(item) + '/' + str(2) + '/let' + str(i) + ' ' + str(j), "PNG")
        y = i * oneHeight
