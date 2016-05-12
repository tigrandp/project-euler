import sys


def factorize(n):
    ret = {}
    i = 2
    while i * i <= n:
        if n % i == 0:
            ret[i] = 0
            while n % i == 0:
                ret[i] += 1
                n /= i
        i += 1

    if n > 1:
        ret[n] = 1

    return ret


def combine(dict_1, dict_2):
    ret = {}
    for key, value in dict_1.items():
        if key in dict_2:
            ret[key] = value + dict_2[key]
        else:
            ret[key] = value
    for key, value in dict_2.items():
        if key not in dict_1:
            ret[key] = value

    return ret

n = 1
while True:
    dict_n = factorize(n)
    dict_n1 = factorize(n + 1)
    d = combine(dict_n, dict_n1)
    d[2] -= 1
    mul = 1
    for key, value in d.items():
        mul *= value + 1
    sys.stderr.write('For %d got %d\n' % (n, mul))
    if mul > 500:
        sys.stdout.write('%d\n' % (n * (n + 1) // 2))
        break
    n += 1
