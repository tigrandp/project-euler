import sys

n = 2000000
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

answer = 0
for i in xrange(1, n):
    if sieve[i]:
        answer += i
    
sys.stdout.write('%d\n' % answer)
