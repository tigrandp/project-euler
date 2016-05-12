import sys

n = 1000000
nth = 10001
sieve = [True] * n

sieve[0] = False
sieve[1] = False

i = 2
while i * i <= n:
    if sieve[i]:
        j = i * i
        while j < n:
            sieve[j] = False
            j += i

    i += 1

counter = 0
answer = -1
for i in xrange(1, n):
    if sieve[i]:
        counter += 1
        if counter == nth:
            answer = i
            break

assert(answer != -1)
sys.stdout.write('%d\n' % answer)
