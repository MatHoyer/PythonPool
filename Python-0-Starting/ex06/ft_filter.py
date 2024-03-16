def ft_filter(func, iterable) -> list:
    '''
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    '''
    if func:
        return [elem for elem in iterable if func(elem)]
    return [elem for elem in iterable if elem]