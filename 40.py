import sys

line = ''
x = 1
while len(line) < 1000000:
    line += str(x)
    x += 1
answer = 1

num = 1

while num <= 1000000:
    answer *= int(line[num - 1])
    num *= 10

sys.stdout.write('%d %d\n' % (x, answer))
