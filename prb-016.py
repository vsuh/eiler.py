# VSCraft
#
"""
задача:  https://projecteuler.net/problem=16
перевод: http://euler.jakumo.org/problems/view/16.html



2^15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.

Какова сумма цифр числа 2^1000?


"""
# solved 13/05/2019 22:29 (1366)

s = str(2 ** 1000)
t = 0
sum = 0
for c in s:
    sum += int(c)
print(sum)
