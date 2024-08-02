
'''Annotate the below function’s parameters
    and return values with the appropriate types
    def element_length(lst):
    return [(i, len(i)) for i in lst]
'''


import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
        typing.List[typing.Tuple[typing.Sequence, int]]:
    '''Create a list of tuples, where each tuple contains a string
        from the input list and its corresponding length,
        and return this list
    '''
    return [(i, len(i)) for i in lst]
