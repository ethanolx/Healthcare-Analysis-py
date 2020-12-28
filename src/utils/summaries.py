from typing import Callable, List, Tuple, Union
import numpy as np

from .switch import switch
from .stats_options import Statistic


def describe(array: np.ndarray, file_name: str, statistics: List[Statistic] = [Statistic.COUNT, Statistic.UNIQUE_COUNT, Statistic.DTYPE], precision: int = 2) -> None:
    """
        Used to generate overall summaries for datasets

        @public
    """
    print('SUMMARY OF DATA\n===============\n')

    print(('File:\t\t' + file_name.split(sep='/')[1]).expandtabs(4))
    print(f'Rows:\t\t{array.shape[0]}'.expandtabs(4))
    print(f'Columns:\t{len(array[0])}'.expandtabs(4))
    print(f'Features:\t{", ".join(array.dtype.fields)}'.expandtabs(
        4), end='\n\n\n')

    _statistical_summary(array=array, stats=statistics, precision=precision)


def _statistical_summary(array: np.ndarray, stats: List[Statistic], precision: int) -> None:
    """
        Used to generate simple numerical summaries for datasets

        @private
    """
    partition_size = 20

    # Construct Table Header
    header: str = '\t'.expandtabs(
        partition_size) + '\t'.join(array.dtype.fields).expandtabs(partition_size)
    header += '\n' + len(header) * '-'

    # Construct Table Body
    body: str = ''

    for row in _select_statistics(array, stats):
        # Statistic Type
        entry = row[0].value + '\t'

        # Values
        entry += '\t'.join(map(lambda x: str(round(x, precision)) if (type(x)
                                                                      is float or type(x) is np.float64) else str(x), row[1]))

        body += entry.expandtabs(partition_size)

        # Next Row
        body += '\n'

    print(header)
    print(body)


def _select_statistics(array: np.ndarray, stats: List[Statistic]) -> List[Tuple[Statistic, List[Union[float, int, None]]]]:
    """
        Used to get functions for selected statistics

        @private
    """
    s: List[Tuple[Statistic, List[Union[float, int, None]]]] = []
    for statistic in stats:
        fn = switch(statistic, {
            Statistic.MIN: (np.min, True),
            Statistic.MAX: (np.max, True),
            Statistic.MEAN: (np.mean, True),
            Statistic.MED: (np.median, True),
            Statistic.Q1: (np.quantile, True, 0.25),
            Statistic.Q3: (np.quantile, True, 0.75),
            Statistic.VAR: (np.var, True),
            Statistic.STD: (np.std, True),
            Statistic.COUNT: (np.count_nonzero, False),
            Statistic.UNIQUE_COUNT: (lambda x: np.count_nonzero(np.unique(x)), False),
            Statistic.DTYPE: (lambda x: x.dtype, False)
        })
        if (len(fn) == 3):
            s.append((statistic, _operation(
                array, lambda arr: fn[0](arr, fn[2]), fn[2])))
        else:
            s.append((statistic, _operation(
                array, lambda arr: fn[0](arr), fn[1])))
    return s


def _operation(array: np.ndarray, fn: Callable[[np.ndarray], Union[int, float]], limit_to_quantitative: bool = True) -> List[Union[float, int, None]]:
    """
        Used to operate on data

        @private
    """
    summary_row: List[Union[float, int, None]] = []
    for col in array.dtype.fields:
        series: np.ndarray = array[col]
        if not limit_to_quantitative or np.issubdtype(series.dtype, np.number):
            summary_row.append(fn(series))
        else:
            summary_row.append(None)
    return summary_row


if __name__ == '__main__':
    print('Description: Module for describing data and producing summary statistics')
