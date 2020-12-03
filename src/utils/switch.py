from typing import Any, Dict
from utils.stats_options import Statistic

def _switch(condition: Statistic, cases: Dict[Statistic, Any]) -> Any:
    return cases[condition]