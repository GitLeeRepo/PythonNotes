#!/usr/bin/python3

# calculates the polynomial for x.  The degree is calculated as the
# number of coefficients - 1.  Output only formatted for up to 5 
# single digit coefficients.  Also illustrates the use of __add__
# and __len__ implementations.

class polynomial:
    __coefs = () # tuple of coefficients

    def __init__(self, *coefs):
        self.__coefs = coefs

    def set_coefs(self, coefs):
        self.__coefs = coefs
        return self.__coefs;

    def get_coefs(self):
        return self.__coefs;

    def for_x(self, x):
        degree = len(self.__coefs) - 1
        j = 0
        result = 0
        for i in range(degree, 0, -1):
            result += self.__coefs[j] * x**i
            j += 1
        return result + self.__coefs[-1]   

    # implement add on two polynomials (i.e, p1 + p2)
    def __add__(self, other):
        # zip makes an iterator that aggregates elements from each of the iterables
        return polynomial(*(x + y for x, y in zip(self.__coefs, other.__coefs))) 

    # implement len() function capabilities 
    def __len__(self):
        return len(self.__coefs)

def main():
    # list of coefficient tuples in multiple degrees
    coefslist = [(2, 2, 2), (3, 3, 3), (4, 4, 4), (2, 2, 2, 2), (3, 3, 3, 3), \
                 (4, 4, 4, 4), (5, 4, 3, 2), (5, 4, 3, 2, 1), (9, 9, 9, 9, 9)]
    p1 = polynomial(*(0,))

    # heading
    print("{:>15}:".format("x = "), end="")
    for i in range(10):
        print("{:5} ".format(i), end="")
    print("")

    # detail - calc for all polynomials for x = 0 thru 9
    for coefs in coefslist:
        print("{:15}:".format(str(coefs)), end="")
        for i in range(10):
            p1.set_coefs(coefs)
            print("{:5} ".format(p1.for_x(i)), end="")
        print("")

    # Add polynomials
    p1 = polynomial(*(1, 2, 3))
    p2 = polynomial(*(4, 5, 6))
    p3 = p1 + p2
    print("\nAdding polynomials:", p1.get_coefs(), "+", p2.get_coefs(), "=", p3.get_coefs())

    print("Polynomial p1 has a length of", len(p1))

if __name__ == "__main__":
    main()
