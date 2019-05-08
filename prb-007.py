# VSCraft
#
"""
https://projecteuler.net/problem=7
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
Какое число является 10001-ым простым числом?
"""
# solved 08.05.2019 14:13 (104743)

n = 2000000
lst=[2]
for i in range(3, n+1, 2):
    if i % 10001 == 0:
        print('{}/{}'.format(i, len(lst)))
    if len(lst) > 10010:
        break
    if (i > 10) and (i % 10 == 5):
        continue
    for j in lst:
        if j*j-1 > i:
            lst.append(i)
            break
        if i % j == 0:
            break
    else:
        lst.append(i)

nn = 0

for i in lst:
    nn += 1
    if nn == 10001:
        print('\n\nRESULT: {}th prime is {}'.format(nn, i))
