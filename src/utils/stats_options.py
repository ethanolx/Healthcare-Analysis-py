from enum import Enum

class Statistic(Enum):
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
    DEFAULT = 'dtype'