import sys
import string

from typing import Callable


def isUpper(char: str) -> bool:
    '''Return True if char is an uppercase letter.'''
    return char in string.ascii_uppercase


def isLower(char: str) -> bool:
    '''Return True if char is a lowercase letter.'''
    return char in string.ascii_lowercase


def isPunctuation(char: str) -> bool:
    '''Return True if char is a punctuation mark.'''
    return char in string.punctuation


def isSpace(char: str) -> bool:
    '''Return True if char is a space.'''
    return char in (' ', '\n')


def isDigit(char: str) -> bool:
    '''Return True if char is a digit.'''
    return char in string.digits


def mySum(text: str, condition: Callable) -> int:
    '''Do a sum of the characters that match the condition.'''
    return len([char for char in text if condition(char)])


def getFirstArg() -> str:
    '''Return args[0] or None if number of argument is > 1.'''
    args = sys.argv[1:]
    try:
        if len(args) > 1:
            raise AssertionError('more than one argument is provided')
        if len(args) == 0:
            try:
                s = input('What is the text to count?\n') + '\n'
                args.append(s)
            except EOFError:
                sys.exit(1)
    except AssertionError as e:
        print(AssertionError.__name__ + ':', e)
        sys.exit(1)
    return args[0]


def parseText(text: str) -> dict:
    '''Parse text and return a dict.'''
    upperLetters = mySum(text, isUpper)
    lowerLetters = mySum(text, isLower)
    punctuations = mySum(text, isPunctuation)
    space = mySum(text, isSpace)
    digits = mySum(text, isDigit)
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
    '''Main function.'''
    text = getFirstArg()
    dictChar = parseText(text)
    formatPrint(dictChar)


if __name__ == '__main__':
    main()
