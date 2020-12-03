from enum import Enum

class Statistic(Enum):
    __order__ = 'COUNT MIN Q1 MEAN MED Q3 STD VAR MAX DTYPE MODE'
    COUNT = 'count'
    MIN = 'min'
    Q1 = 'Q1'
    MEAN = 'mean'
    MED = 'med'
    Q3 = 'Q3'
    STD = 'std'
    VAR = 'var'
    MAX = 'max'
    DTYPE = 'dtype'
    MODE = 'mode'

import numpy as np
a: np.ndarray = np.array([1, 2, 3, 3, 2])
print(np.bincount(a))