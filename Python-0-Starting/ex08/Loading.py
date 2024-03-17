def ft_tqdm(lst: range):
    total = len(lst)
    for i, elem in enumerate(lst):
        percent = int((i + 1) * 100 / total)
        print(f'\r{percent}%|[' + percent * '=' +
              (100 - percent) * ' ' + f']| {i + 1}/{total}', end='')
        yield elem
