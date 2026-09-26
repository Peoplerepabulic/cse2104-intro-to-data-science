import io
import warnings
import itertools
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from os.path import exists
from contextlib import redirect_stdout


def load_image(path):
    '''Loads image at PATH'''
    return plt.imread(path)

def show_array_as_image(arr):
    plt.imshow(arr, cmap='gray')
    plt.clim(0, 1)
