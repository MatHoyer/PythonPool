def mean(lst: list):
    print(sum(lst) / len(lst))


def median(lst: list):
    print(lst[len(lst) // 2])


def quartile(lst: list):
    first = len(lst) // 4
    last = len(lst) - first - 1
    print([float(lst[first]), float(lst[last])])


def std(lst: list):
    mean = sum(lst) / len(lst)
    ecaAll = sum((mean - el)**2 for el in lst)
    print((ecaAll / len(lst))**(0.5))


def var(lst: list):
    mean = sum(lst) / len(lst)
    ecaAll = sum((mean - el)**2 for el in lst)
    print(ecaAll / len(lst))


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
        func(lst)

    return