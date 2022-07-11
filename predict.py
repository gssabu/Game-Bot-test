"""
This file will make a prediction based on the input data.
Author: Arda Mavi
"""
import cv2
from PIL import Image
from numpy import size


def predict(model, x):
    """
    This function will make a prediction based on the input data.
    :param model: Which model to use.
    :param X: input data.
    :return: y_pred: prediction.
    """
    # resize it with PIL, because scipy.misc.imresize is deprecated.
    #x = X(Image.fromarray(X).resize((size[0] * 4, size[1] * 4),
    #                               resample=Image.BICUBIC))
    width = 150
    height = 150
    dim = (width, height)
    x = cv2.resize(x, dim, interpolation=cv2.INTER_AREA)
    y = model.predict(x.reshape(1, 150, 150, 3))
    y = y.argmax()
    return y
