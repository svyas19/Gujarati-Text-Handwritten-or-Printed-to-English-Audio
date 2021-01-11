import os
import numpy as np
import pandas as pd
from PIL import Image


MODULE_FOLDER = os.path.dirname(__file__)


def create_dataset_csv(mode='train'):
    if mode == 'train':
        data_root_dir = MODULE_FOLDER + '/../data-set/clean/training/images/'
        output_file = MODULE_FOLDER + '/../data-set/clean/training/dataset.csv'
    elif mode == 'test':
        data_root_dir = MODULE_FOLDER + '/../data-set/clean/testing/images/'
        output_file = MODULE_FOLDER + '/../data-set/clean/testing/dataset.csv'
    else:
        return None

    col = ['label']
    for i in range(0, 784):
        col.append('pixel' + str(i))

    df = pd.DataFrame(columns=col)
    numbers = 60

    for number in range(numbers):
        print(number)
        for item in os.listdir(data_root_dir + str(number)):
            im = Image.open(data_root_dir + str(number) + '/' + item).convert('L')
            pixel_numpy_array = np.array(im.getdata())
            flat_pixel = pixel_numpy_array.flatten()

            data = [number]
            for pixel in flat_pixel:
                data.append(pixel)
            df = df.append(pd.Series(data, index=col), ignore_index=True)

    df.to_csv(output_file, encoding='utf-8')


create_dataset_csv(mode='train')
# create_dataset_csv(mode='test')
