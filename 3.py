import sys

number = long(600851475143)

i = 2
answer = 1

while i * i <= number:
    while number % i == 0:
        answer = max(answer, i)
        number //= i
    i = i + 1

answer = max(answer, number)

sys.stdout.write('%d\n' % answer)
