import sys
import string

if len(sys.argv) == 3:
    try:
        int(sys.argv[2])
    except ValueError:
        print("Wrong argument: integer is needed")
        exit(1)
    aux1 = sys.argv[1:]
    aux2 = aux1[0].split(' ')
    aux3 = []
    aux4 = []
    mydict = str.maketrans('', '', string.punctuation)

    for x in aux2:
        aux3.append(x.translate(mydict))

    for x in aux3:
        if len(x) > int(aux1[1]):
                aux4.append(x)

    print("{}".format(aux4))
else:
    print("ERROR")

