import cv2
import os


MODULE_FOLDER = os.path.dirname(__file__)

TEN = 10
os.mkdir(MODULE_FOLDER + '/../data-set/unclean/counterdetection/' + str(TEN) + '_crop')

for i in os.listdir(str(TEN) + '/'):
    flag = 0
    a = None
    temp_a = None
    image = cv2.imread(str(TEN) + '/' + i)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # grayscale
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # threshold
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    dilated = cv2.dilate(thresh, kernel, iterations=13)  # dilate
    _, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # get contours for each contour found, draw a rectangle around it on original image

    for contour in contours:
        # get rectangle bounding contour
        [x, y, w, h] = cv2.boundingRect(contour)
        # discard areas that are too large
        if h > 120 or w > 120:
            continue
        # discard areas that are too small
        if h < 30 or w < 30:
            continue

        # draw rectangle around contour on original image
        try:
            a = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)
            temp_a = a[y:y + h, x:x + w]

        except Exception as e:
            print('Error: ')
            print(e)
            # Do nothing
            print('*******************************************' + str(i))
            print("\n")
        else:
            # write original image with added contours to disk
            flag = 1
            cv2.imwrite(MODULE_FOLDER + '/../data-set/unclean/counterdetection' + str(TEN) + '/' + i, a)
            cv2.imwrite(MODULE_FOLDER + '/../data-set/unclean/counterdetection/' + str(TEN) + '_crop' + '/' + i, temp_a)

    if flag == 1:
        os.remove(MODULE_FOLDER + '/../data-set/unclean/counterdetection' + str(TEN) + '/' + i)
