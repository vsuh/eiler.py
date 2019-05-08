# VSCraft
#
"""
https://projecteuler.net/problem=15
Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо, существует
ровно 6 маршрутов до правого нижнего угла сетки.

Сколько существует таких маршрутов в сетке 20×20?

"""
# solving ..(137846528820)
def combinator(num):
    import math
    return math.factorial(2 * num) / (math.factorial(num) * math.factorial(num))
    # 2N! / (N! * N!)


print(combinator(20))