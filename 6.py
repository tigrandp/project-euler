import sys

sum_squares = 0
square_sum = 0

for i in xrange(0, 101):
    sum_squares += i * i
    square_sum += i

square_sum = square_sum * square_sum

sys.stdout.write('%d\n' % (square_sum - sum_squares))
