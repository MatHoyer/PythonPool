import sys
import string
import termios
import tty


def getFirstArg() -> str:
    '''Return args[0] or exit if number of argument is > 1.'''
    args = sys.argv[1:]
    try:
        if len(args) > 1:
            raise AssertionError('more than one argument is provided')
        if len(args) == 0:
            s = ''
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            print('Please enter a text:')
            try:
                tty.setraw(sys.stdin.fileno())
                while True:
                    char = sys.stdin.read(1)
                    if char == '\x04':
                        if len(s) == 0:
                            termios.tcsetattr(fd, termios.TCSADRAIN,
                                              old_settings)
                            raise AssertionError('no text provided')
                        break
                    s += char
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    if char == '\x0d':
                        print(s)
                        break
            finally:
                args.append(s)
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
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
