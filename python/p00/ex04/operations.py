import sys
import math


assert len(sys.argv) <= 3, "More arguments than needed are provided"


try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    print("Sum:         ", a + b) 
    print("Difference:  ", a - b)
    print("Product:     ", a * b)
    if (b == 0):
        print("Quotient:    ERROR (division by zero)")
        print("Remainder:   ERROR (modulo by zero)")
    else:
        print("Quotient:    ", a / b)
        print("Remainder:   ", a % b)
except ValueError:
    print("Not an integer")
except IndexError:
    print("Need more arguments")
