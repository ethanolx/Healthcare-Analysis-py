from enum import Enum


class Statistic(Enum):
    """
        Enum containing the various statistical operations supported

        @public
    """
    __order__ = 'COUNT UNIQUE_COUNT MIN Q1 MEAN MED Q3 STD VAR MAX DTYPE'
    COUNT = 'count'
    UNIQUE_COUNT = 'unique'
    MIN = 'min'
    Q1 = 'Q1'
    MEAN = 'mean'
    MED = 'med'
    Q3 = 'Q3'
    STD = 'std'
    VAR = 'var'
    MAX = 'max'
    DTYPE = 'dtype'
