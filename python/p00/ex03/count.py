import sys
import math
import string

def text_analyzer(text = None):
    '''This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text.
    '''
    if (text == None):
        text = input("What's the text to analyze? ")
    if not(isinstance(text, str)):
        print("Error: is not a string")
        return
    ch = 0
    up = 0
    low = 0
    punt = 0
    spac = 0

    print(type(text))
    up = sum(1 for c in text if c.isupper())
    low = sum(1 for c in text if c.islower())
    punt = sum(1 for c in text if c in string.punctuation)
    spac = sum(1 for c in text if c in (' ', '\t', '\n', '\r', '\v', '\f'))

    print("The text contains ", ch, " character(s):")
    print("- ", up, " upper letter(s)")
    print("- ", low, " lower letter(s)")
    print("- ", punt, " punctuation mark(s)")
    print("- ", spac, " space(s)")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if (isinstance(sys.argv[1], str)):
            text_analyzer(sys.argv[1])
    elif (len(sys.argv) == 1):
            text_analyzer()
    else:
        print("More arguments than needed are provided")

'''
print(add_numbers(5, 10))
print(add_numbers.__doc__)

val = input("Enter your value: ")
print(val)
'''



'''
 for element in text:
        ch += 1
        if ((element != " ") and not(isupper(element)) and not(islower(element))):
            punt += 1
        else:
            up += isupper(element)
            low += islower(element)
            spac += element == " "
'''
