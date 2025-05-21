def square(x: int | float) -> int | float:
    '''Calculates the square of a number'''
    return x**2


def pow(x: int | float) -> int | float:
    '''Calculates the power of a number'''
    return x**x


def outer(x: int | float, function) -> object:
    '''Return a function that applyies the function to the number x'''
    mem = x
    def inner() -> float:
        nonlocal mem
        mem = function(mem)
        return mem
    return inner