import sys

sm = 0
mul = 1
for i in xrange(1, 101):
    mul *= i
    while mul % 10 == 0:
        mul /= 10

sys.stdout.write('%s\n' % (sum([int(i) for i in str(mul)])))
