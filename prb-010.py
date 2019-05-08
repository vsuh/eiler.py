# VSCraft
#
"""
https://projecteuler.net/problem=10
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов.

"""
# solved 08.05.2019 14:28 (142913828922)
MAX = 2000000
SUM = 0


def simple_list(n):
    lst = [2]
    for i in range(3, n, 2):
        if i % 100001 == 0:
            print('{}/{}'.format(i, len(lst)))
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


s: int
for s in simple_list(MAX):
    SUM += s

print('\n\nResult: {}'.format(SUM))