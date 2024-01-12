#!/usr/bin/env python3
"""8. Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """8. Complex types - functions"""

    def multi(x: float) -> float:
        return x * multiplier

    return multi
