import tensorflow as tf
from PIL import Image
import numpy as np
import os

from preprocessing.predict_contour_preprocess import detect_contour

MODULE_FOLDER = os.path.dirname(__file__)


def predict(filepath):
    #detect_contour(filepath)
    img = Image.open(filepath).convert('L')
    img = img.resize((28, 28))
    img.show()
    im2arr = np.array(img)

    flat_pixel = im2arr.flatten()
    flat_pixel = flat_pixel.astype(np.float)
    images = np.multiply(flat_pixel, 1.0 / 255.0)
    im2arr = images.reshape(1, 28, 28, 1)

    model = tf.keras.models.load_model(MODULE_FOLDER + '/../models/model.h5')
    result = model.predict(im2arr)[0]
    class_ = model.predict_classes(im2arr)
    confidence = round(result[class_][0] * 100, 2)

    return confidence, class_
