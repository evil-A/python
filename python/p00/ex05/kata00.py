import sys

kata = (19,42,21)

print("The {} numbers are:".format(len(kata)), ", ".join([str(item) for item in kata]))
print("The %i numbers are: %i, %i, %i" % (len(kata), *kata))
print("The {} numbers are: {}, {}, {}".format(len(kata), *kata))
