def slice_me(family: list, start: int, end: int) -> list:
    try:
        int(start), int(end)
        
    except ValueError as e:
        print(ValueError.__name__, ':', e)
        exit(1)