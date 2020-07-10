"""
Fermat’s famous theorem claims that for any n>2, there are
no three positive integers a, b, and c such that: a**n + b**n = c**n

here is a checker for this:

check_fermat takes in 4 arguments, a b c n,

a,b,c are the three coefficients, and n is the power
"""


def check_fermat(a, b, c, n):
    "check_fermat takes in 4 arguments, a,b,c are the three coefficients, and n is the power "

    if n > 2 and a**n + b**n == c**n:
        print("Found a case for n>2!")
    else:
        print("Nope, try something else!")
