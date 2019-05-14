# VSCraft
#
"""
задача:  https://projecteuler.net/problem=20
перевод: http://euler.jakumo.org/problems/view/20.html

n! означает n × (n − 1) × ... × 3 × 2 × 1

Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Найдите сумму цифр в числе 100!.


"""
# solved 14.05.2019 11:59 (648)

import math

f = math.factorial(100)
print('{}'.format(f))
s = str(f)
n = 0
for c in s:
    n += int(c)

print(n)
