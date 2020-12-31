# Type Checking
from typing import Any, Dict

def switch(condition: Any, cases: Dict[Any, Any]) -> Any:
    """
        Meant to simulate a regular switch-case block

        @protected
    """
    return cases[condition]
