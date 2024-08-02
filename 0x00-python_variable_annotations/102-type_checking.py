#!/usr/bin/env python3
"""Use mypy to validate the following piece of code
and apply any necessary changes.
"""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List[Any]:
    """Creates a zoomed-in version of the input tuple by repeating each element
    a specified number of times.

    Args:
        lst: A tuple of elements to be zoomed in.
        factor: An integer indicating how many times each element in the tuple
                should be repeated. Default is 2.

    Returns:
        A list where each element from the input tuple is repeated
        'factor' times.
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
