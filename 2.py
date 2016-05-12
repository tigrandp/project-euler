import sys

prev = 1
answer = 0
prev_prev = 1

while True:
    next_val = prev + prev_prev
    if next_val > 4 * 10**6:
        break
    if next_val % 2 == 0:
        answer += next_val
    prev_prev = prev
    prev = next_val

sys.stdout.write('%d\n' % answer)
