import sys
from ft_filter import ft_filter
import string


def isPunctuation(c: str) -> bool:
    '''
    Return True if the character is a punctuation, False otherwise.
    '''
    return c not in string.punctuation


def strPrintable(s: str) -> bool:
    '''
    Return True if all characters in the string are printable
    or the string is empty, False otherwise.
    '''
    return all([c.isprintable() and isPunctuation(c) for c in s])


def main():
    '''
    Main function to run the program.
    It takes two arguments from the command line
    and prints the result of ft_filter function.
    If the arguments are bad, it prints an error message and exits with code 1.
    '''
    args = sys.argv[1:]
    try:
        if len(args) != 2:
            raise AssertionError('the arguments are bad')
        try:
            text = args[0]
            if strPrintable(text) is False:
                raise AssertionError('the first argument is not a good string')
            size = int(args[1])
        except ValueError:
            raise AssertionError('the second argument is not a number')
        # print(list(filter(lambda x: len(x) >= size, text.split())))
        print(list(ft_filter(lambda x: len(x) >= size, text.split())))
    except AssertionError as e:
        print(AssertionError.__name__ + ':', e)
        exit(1)


if __name__ == '__main__':
    main()
