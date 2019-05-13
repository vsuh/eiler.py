# VSCraft
#
"""
https://projecteuler.net/problem=12
Последовательность треугольных чисел образуется путем сложения натуральных чисел. К примеру, 7-ое треугольное
число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. Первые десять треугольных чисел:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Перечислим делители первых семи треугольных чисел:

 1: 1
 3: 1, 3
 6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28
Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.

Каково первое треугольное число, у которого более пятисот делителей?


"""
# solving ..

import math
import time


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield int(divisor)


def cont(org_num):
    return len(list(divisorGenerator(org_num)))


ii =0
ss = 0
cnt = True
while cnt:
    ii += 1
    ss += ii
    dvs = cont(ss)
    if dvs > 500:
        print(ii, ss, dvs)
        cnt = False
    if ii % 10000 == 0:
        print(time.strftime('%H:%M:%S'), ii, ss, dvs)

