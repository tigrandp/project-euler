import sys


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a * (b // gcd(a, b))

answer = 1

for i in xrange(2, 21):
    answer = lcm(answer, i)

sys.stdout.write('%d\n' % answer)
