import sys


n = 20


def factorial(m):
    mul = 1
    for i in xrange(1, m + 1):
        mul *= i
    return mul

sys.stdout.write('%s\n' % (factorial(n + n) // factorial(n) // factorial(n)))
