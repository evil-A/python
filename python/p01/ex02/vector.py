class Vector:
    def __init__(self, values):
        if isinstance(values, list):
            if len(values) > 1:
                for elem in values:
                    if isinstance(elem, list):
                        for el in elem:
                            if not isinstance(el, float):
                                print("ERROR: bad input")
                                exit (1)
                    else:
                        print("ERROR: bad input")
                self.values = values
                self.shape = (len(values), 1)
            elif len(values) == 1:
                if isinstance(values[0], list):
                    for elem in values[0]:
                        if not isinstance(elem, float):
                            print("ERROR: bad input")
                            exit (1)
                    self.values = values
                    self.shape = (1, len(values[0]))
                else:
                    print("ERROR: bad input")
            print(self.values)###
            print(self.shape)###

    def __str__(self):
        return "Vector({})".format(str(self.values))


"""
def dot():
def T():
__add__
__radd__
# add & radd : only vectors of same shape.
__sub__
__rsub__
# sub & rsub: only vectors of same shape.
__truediv__
# truediv : only with scalars (to perform division of Vector by a scalar).
__rtruediv__
# rtruediv : raises an NotImplementedError with the message "Division of a scalar by a Vector is not defined here."
__mul__
__rmul__
# mul & rmul: only scalars (to perform multiplication of Vector by a scalar).
__str__
__repr__
# must be identical, i.e we expect that print(vector) and vector within python interpretor behave the same, see correspond
"""
