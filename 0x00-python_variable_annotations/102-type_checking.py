#!/usr/bin/env python3
'''Use mypy to validate the following piece of code
    and apply any necessary changes.

def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)'''


from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Creates a zoomed-in version of the input tuple by repeating each element
    a specified number of times.
    Args:
        lst: A tuple of integers to be zoomed in.
        factor: An integer indicating how many times each element in the tuple
                should be repeated. Default is 2.
    Returns:
        A list of integers where each element from the input tuple is repeated
        'factor' times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]  # This should be a list

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
