import sys
import math

txt = "Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3"
if len(sys.argv) != 3:
    print(txt)
else:
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
        print(txt)

