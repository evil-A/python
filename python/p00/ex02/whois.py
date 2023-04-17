import sys

assert len(sys.argv) < 3, "More arguments than needed are provided"
#assert len(sys.argv) != 1, "Not enough arguments"

try:
    int(sys.argv[1])
    if (int(sys.argv[1]) == 0):
        print("I'm zero")
    elif ((int(sys.argv[1]) % 2) == 0):
        print("I'm even")
    elif ((int(sys.argv[1]) % 2) != 0):
        print("I'm odd")
except ValueError:
    print("Not an integer")
except IndexError:
    print("Not enough arguments")

