import sys
import string


def getFirstArg() -> str:
    '''Return args[0] or exit if number of argument is > 1.'''
    args = sys.argv[1:]
    try:
        if len(args) > 1:
            raise AssertionError('more than one argument is provided')
        if len(args) == 0:
            try:
                s = input('What is the text to count?\n') + '\n'
                args.append(s)
            except EOFError:
                exit(1)
    except AssertionError as e:
        print(AssertionError.__name__ + ':', e)
        exit(1)
    return args[0]


def parseText(text: str) -> dict:
    '''Parse text and return a dict.'''
    upperLetters = sum(1 for c in text if c.isupper())
    lowerLetters = sum(1 for c in text if c.islower())
    punctuations = sum(1 for c in text if c in string.punctuation)
    space = sum(1 for c in text if c.isspace())
    digits = sum(1 for c in text if c.isdigit())
    return {
        'characters': len(text),
        'upper letters': upperLetters,
        'lower letters': lowerLetters,
        'punctuations marks': punctuations,
        'spaces': space,
        'digits': digits
    }


def formatPrint(dictChar: dict) -> None:
    '''Print the dict in a pretty way.'''
    for key, value in dictChar.items():
        if key == 'characters':
            print(f'The text contains {value} {key}')
        else:
            print(f'{value} {key}')


def main():
    '''Parse the text and print the result.'''
    text = getFirstArg()
    dictChar = parseText(text)
    formatPrint(dictChar)


if __name__ == '__main__':
    main()
