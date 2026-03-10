import numpy as np


def translation_matrix(a,b):
    T = np.array([
        [1, 0, a],
        [0, 1, b],
        [0, 0, 1]
    ], dtype=float)
    
    return T