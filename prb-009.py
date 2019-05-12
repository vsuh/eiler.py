# VSCraft
#
"""
https://projecteuler.net/problem=9
Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство

a^2 + b^2 = c^2
Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.

"""
# solved 08.05.2019 15:15 (31875000)
MAX = 1000

def solution(SUM):
    for a in range(1,SUM):
        aa = a**2
        # if aa>999:
        #     break
        for b in range(1,SUM):
            bb = b**2
            # if bb > 999:
            #     break
            dd = aa + bb
            # print('a({}) + b({}) = {} '.format(a**2, b**2, dd))
            for c in range(1, SUM):
                if dd == c ** 2:
                    print('{}^2({}) + {}^2({}) = {}^2({}) a+b+c = {}'.format(a, a ** 2, b, b ** 2, c, c ** 2, (a + b + c)))
                    if (a + b + c) == SUM:
                        print('Result:  a^2({}) + b^2({}) = c^2({}) a*b*c = {}'.format(a ** 2, b ** 2, c ** 2, (a*b*c)))
                        return [a,b,c]


result = 1
for n in solution(MAX):
    result *= n

print(result)
