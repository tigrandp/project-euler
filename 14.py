import sys

memo = {}


def go(num):
    if num in memo:
        return memo[num]
    if num % 2 == 0:
        memo[num] = 1 + go(num / 2)
    else:
        memo[num] = 1 + go(3 * num + 1)

    return memo[num]

memo[1] = 1

answer = 0
for i in xrange(1, 1000001):
    res = go(i)
    if res > answer:
        answer = res
        who = i


sys.stdout.write('%d %d\n' % (answer, who))
