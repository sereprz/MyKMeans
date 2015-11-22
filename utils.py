import numpy as np


def sum_of_squares(v, w):
    return np.sum(
        [(v_i - w_i)**2 for (v_i, w_i) in zip(v, w)])
