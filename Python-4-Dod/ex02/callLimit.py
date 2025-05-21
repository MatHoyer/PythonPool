def callLimit(limit: int):
    '''Decorator to limit the number of calls to a function'''
    count = 0

    def callLimiter(function):
        def limit_function(*args, **kwds):
            nonlocal count
            if count >= limit:
                print('Error:', function, 'call too many times')
                return
            count += 1
            return function(*args, **kwds)
        return limit_function

    return callLimiter
