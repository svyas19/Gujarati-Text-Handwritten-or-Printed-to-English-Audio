import os
import pandas as pd
import numpy as np
from keras import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from keras.utils import np_utils


MODULE_FOLDER = os.path.dirname(__file__)

NO_OF_CLASSES = 60
EPOCHS = 30
BATCH_SIZE = 200


def load_data(mode='train'):
    if mode == 'test':
        data = pd.read_csv(MODULE_FOLDER + '/../data-set/clean/testing/dataset.csv', encoding='utf-8')
    else:
        data = pd.read_csv(MODULE_FOLDER + '/../data-set/clean/training/dataset.csv', encoding='utf-8')

    # Extracting images and labels from given data for images
    images = data.iloc[:, 2:].values
    images = images.astype(np.float)

    # Normalize from [0:255] => [0.0:1.0] and reshape.
    images = np.multiply(images, 1.0 / 255.0)
    images = images.reshape(images.shape[0], 28, 28, 1)

    # For labels
    labels_flat = np_utils.to_categorical(data[['label']].values.ravel())

    return images, labels_flat


def cnn():
    model = Sequential()
    model.add(Conv2D(32, (5, 5), input_shape=(28, 28, 1), activation='relu', padding='same'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(16, (3, 3), activation='relu', padding='same'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(50, activation='relu')                                                                                                                                          =)
    model.add(Dense(NO_OF_CLASSES, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    print(model.summary())c
    return model


def train():
    x_train, y_train = load_data(mode='train')
    # x_test, y_test = load_data(mode='test')

    model = cnn()
    model.fit(x_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE)
    # metrics = model.evaluate(x_test, y_test)
    # print(metrics)

    # Save model.
    model.save(MODULE_FOLDER + '/../models/model.h5')


train()
