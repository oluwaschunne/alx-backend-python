#!/usr/bin/env python3
"""12. Type Checking"""
# filename: 102-type_checking.py

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """12. Type Checking"""
    zoomed_in: Tuple = tuple([item for item in lst for i in range(factor)])
    return list(zoomed_in)


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
