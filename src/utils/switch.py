from typing import Any, Dict

def _switch(condition: Any, cases: Dict[Any, Any]) -> Any:
    return cases[condition]