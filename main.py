import decimal
from math  importfactorial

def pi(c):
    decimal.getcontext().prec = n + 1
    k = 0
    result = 0
    next = 426880 * decimal.Decimal('10005').sqrt()
    a = factorial(6 * k)
    b = 545140134 * k + 13591409
    top = a * b
    n = factorial(3 * k)
    d = factorial(k) ** 3
    e = (-262537412640768000) ** k
    bottom = decimal.Decimal(n * d * e)
    result += top / bottom
    return print(next / result)
