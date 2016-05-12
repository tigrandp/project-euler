import sys

answer = 0

for num1 in xrange(100, 1000):
    for num2 in xrange(100, 1000):
        str1 = str(num1 * num2)
        str2 = str1[::-1]
        if str1 == str2:
            answer = max(answer, num1 * num2)

sys.stdout.write('%d\n' % answer)
