class Complex:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    """
    From the review...
    """
    # def add_complex(self, other_complex):
    #     real_part = self.real + other_complex.real
    #     imaginary_part = self.imaginary + other_complex.imaginary
    #     summ = Complex(real_part, imaginary_part)
    #
    #     return summ
    #
    # def sub_complex(self, other_complex):
    #     real_part = self.real - other_complex.real
    #     imaginary_part = self.imaginary - other_complex.imaginary
    #     difference = Complex(real_part, imaginary_part)
    #
    #     return difference
    #
    # def mult_complex(self, other_complex):
    #     real_part = self.real * other_complex.real - self.imaginary * other_complex.imaginary
    #     imaginary_part = self.real * other_complex.imaginary - self.imaginary * other_complex.real
    #     product = Complex(real_part, imaginary_part)
    #
    #     return product
    """
    Arithmetic Operators...(all assume that "other" is also an object of the Complex class)
    """
    def __add__(self, other):
        """
        Addition
        (a + bi) + (c + di) = (a + c) + (b + d)i
        """
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return Complex(real_part, imaginary_part)

    def __sub__(self, other):
        """
        Subtraction
        (a + bi) - (c + di) = (a - c) + (b - d)i
        """
        real_part = self.real - other.real
        imaginary_part = self.imaginary - other.imaginary
        return Complex(real_part, imaginary_part)

    def __mul__(self, other):
        """
        Multiplication
        (a + bi) • (c + di) = (ac - bd) + (ad + bc)i
        """
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary - self.imaginary * other.real
        product = Complex(real_part, imaginary_part)

        return product

    """
    Comparison Operators...(all assume that "other" is also an object of the Complex class)
    """
    def __eq__(self, other):
        """
        Equality
        """
        return self.real == other.real and self.imaginary == other.imaginary

    def __gt__(self, other):
        """
        Greater than
        """
        if self.real > other.real:
            return True
        elif self.real == other.real and self.imaginary > other.imaginary:
            return True
        else:
            return False

    def __ne__(self, other):
        """
        Inequality
        """
        return not (self == other)

    def __ge__(self, other):
        """
        Greater than or equal
        """
        return self > other or self == other

    def __lt__(self, other):
        """
        Less than
        """
        return not (self >= other)

    def __le__(self, other):
        """
        Less than or equal
        """
        return self < other or self == other

    """
    String Representations...
    """
    def __str__(self):
        return "{} {} {}i".format(self.real,
                                  "+" if self.imaginary >= 0.0 else "-",
                                  self.imaginary if self.imaginary >= 0 else abs(self.imaginary))

    def __repr__(self):
        return str(self)  # taking advantage of the __str__() implementation


def main():
    complex_a = Complex(42, 77.0)
    complex_b = Complex(0.5, -25.0)

    print(complex_a)
    print(complex_b)

    summ = complex_a + complex_b
    diff = complex_a - complex_b
    prod = complex_a * complex_b

    print("Sum: {}\nDifference: {}\nProduct: {}".format(summ, diff, prod))

    print("({} == {}) -> {}".format(complex_a, complex_b, complex_a == complex_b))
    print("({} > {}) -> {}".format(complex_a, complex_b, complex_a > complex_b))
    print("({} != {}) -> {}".format(complex_a, complex_b, complex_a != complex_b))
    print("({} >= {}) -> {}".format(complex_a, complex_b, complex_a >= complex_b))
    print("({} < {}) -> {}".format(complex_a, complex_b, complex_a < complex_b))
    print("({} <= {}) -> {}".format(complex_a, complex_b, complex_a <= complex_b))

    # REPR:
    complex_numbers = [Complex(imaginary=1.0, real=20.0), Complex(), Complex(0.005, 25.4)]

    print(complex_numbers)


main()
