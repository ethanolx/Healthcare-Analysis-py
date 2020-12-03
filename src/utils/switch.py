from typing import Any, Dict
from utils.stats_options import Statistic

def _switch(condition: Statistic, cases: Dict[Statistic, Any]):
    if condition in cases.keys():
        return cases[condition]
    else:
        return cases[Statistic.DEFAULT]