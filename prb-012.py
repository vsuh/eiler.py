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
from colorama import Fore, Style
from typing import List, Any

DIVS = 50

def divisors(n):
    large_divs = []
    for i in range(1, 1+int(math.sqrt(n))):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divs.append(n / i)
    for div in reversed(large_divs):
        yield div

def count_divs(ss):
    dividers = 0
    # print(ss, ':', end=' ')
    for i in range(int(ss/2)+1, 1, -1):
        if ss % i == 0:
            dividers += 1
            # print(i, end=' ')
    # print('')
    return dividers

#
cnt = True
ii = 0
ss = 0
while cnt:
    ii += 1
    ss = ss + ii
    ee = list(divisors(ss))
    if len(ee) >= DIVS:
        cnt = True
    if ii == 2 or ii % 10000 == 0:
        print(time.strftime('%H:%M:%S'), ii, ':', ss, '\\\\', len(ee))
else:
    print('number {}{}{} has more than 500 divisors ({}) : {}'.format(Fore.LIGHTYELLOW_EX, ss, Fore.RESET, len(ee), list(ee)))

# print(list(divisors(100000000)))