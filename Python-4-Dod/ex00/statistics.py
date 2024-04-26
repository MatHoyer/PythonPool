def mean(lst: list):
    return (sum(lst) / len(lst))


def median(lst: list):
    return (lst[len(lst) // 2])


def quartile(lst: list):
    first = len(lst) // 4
    last = len(lst) - first - 1
    return ([float(lst[first]), float(lst[last])])


def calcVariance(lst: list):
    mean = sum(lst) / len(lst)
    ecaAll = sum((mean - el)**2 for el in lst)
    return ecaAll / len(lst)


def std(lst: list):
    return ((calcVariance(lst))**(0.5))


def var(lst: list):
    return (calcVariance(lst))


def ft_statistics(*args, **kwargs):
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
        print(func(lst))

    return