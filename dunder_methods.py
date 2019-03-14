# some behaviour that I want to implement, I just create __ function __
# top level function or some syntax, we create corresponding __ function __
"""This is my Polynomial Class!!"""


class Polynomial:
    """Class representation of a Polynomial"""

    def __init__(self, *coeffs) -> None:
        self.coeffs = coeffs

    def __repr__(self):
        return "Polynomial({})".format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)


p1: Polynomial = Polynomial(3, 4, 5)
p2: Polynomial = Polynomial(1, 2, 3)
