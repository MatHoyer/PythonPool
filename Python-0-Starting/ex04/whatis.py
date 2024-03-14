import sys

args = sys.argv

try:
    if len(args) > 2:
        raise AssertionError('more than one argument is provided')
    else:
        if len(args) == 2:
            try:
                arg = int(args[1])
                if arg % 2 == 0:
                    print('I\'m Even.')
                else:
                    print('I\'m Odd.')
            except ValueError:
                raise AssertionError('argument is not an integer')
except AssertionError as e:
    print(AssertionError.__name__ + ':', e)