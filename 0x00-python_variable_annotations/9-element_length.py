
'''Annotate the below function’s parameters
    and return values with the appropriate types
    def element_length(lst):
    return [(i, len(i)) for i in lst]
'''


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    '''Create a list of tuples, where each tuple contains a string
        from the input list and its corresponding length,
        and return this list
    '''
    return [(i, len(i)) for i in lst]
