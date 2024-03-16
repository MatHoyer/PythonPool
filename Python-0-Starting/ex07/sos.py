import sys


NESTED_MORSE = {
    ' ': '/ ', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.'
}


def checkArgs(text: str) -> bool:
    '''
    Return True if the text is alnum, False otherwise.
    '''
    return all([c.isalnum() or c == ' ' for c in text])


def toMorseCode(text: str) -> str:
    return str(' '.join([NESTED_MORSE[c.upper()] for c in text]))


def main():
    '''
    Take one argument from the command line and convert it to Morse code.
    If more than one argument is given, print an error message and exit.
    '''
    args = sys.argv[1:]
    try:
        if len(args) != 1 or checkArgs(args[0]) is False:
            raise AssertionError(": the arguments are bad.")
        print(toMorseCode(args[0]))
    except AssertionError as e:
        print(AssertionError.__name__ + ':', e)
        exit(1)


if __name__ == "__main__":
    main()
