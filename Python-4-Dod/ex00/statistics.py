def mean(lst: list):
    '''Calculates the mean of a list of numbers'''
    return (sum(lst) / len(lst))


def median(lst: list):
    '''Calculates the median of a list of numbers'''
    return (lst[len(lst) // 2])


def quartile(lst: list):
    '''Calculates the first and third quartile of a list of numbers'''
    first = len(lst) // 4
    last = len(lst) - first - 1
    return ([float(lst[first]), float(lst[last])])


def calcVariance(lst: list):
    '''Calculates the variance of a list of numbers'''
    meanVar = mean(lst)
    ecaAll = sum((meanVar - el)**2 for el in lst)
    return ecaAll / len(lst)


def std(lst: list):
    '''Calculates the standard deviation of a list of numbers'''
    return ((calcVariance(lst))**(0.5))


def var(lst: list):
    '''Calculates the variance of a list of numbers'''
    return (calcVariance(lst))


def ft_statistics(*args, **kwargs):
    '''Calculates all stats of a list of numbers'''
    lst = None
    if args:
        lst = list(args)
        lst.sort()
    for value in kwargs.values():
        switcher = {
            "mean": mean,
            "median": median,
            "quartile": quartile,
            "std": std,
            "var": var
        }
        func = switcher.get(value)
        if not func:
            return
        if not args:
            print("ERROR")
            continue
        print(value, ':', func(lst))

    return
