#!/usr/bin/env python3
"""
7. Complex types - string and int/float to tuple
mandatory
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    7. Complex types - string and int/float to tuple
    mandatory
    """
    return tuple([k, float(v * v)])
