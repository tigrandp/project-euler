import sys

for a in xrange(0, 1000):
    for b in xrange(a + 1, 1000):
        c = a * a + b * b
        for c in xrange(b + 1, 1000):
            if a * a + b * b != c * c:
                continue
            if a + b + c == 1000:
                sys.stderr.write('%d %d %d\n' % (a, b, c))
                sys.stdout.write('%d\n' % (a * b * c))
