import sys
import string

morse = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ' ': '/'
        }

assert len(sys.argv) > 1, "More arguments are needed"

aux1 = ''
aux2 = ''

for item in sys.argv[1:]:
    aux1 = (aux1 + ' ' + item).lstrip(' ').upper()
for x in aux1:
    if not x in morse.keys():
        print("ERROR")
        exit(1)
    else:
        aux2 = aux2 + ' ' + morse[x]

print(aux2)

