# VSCraft
'''
задача:  https://projecteuler.net/problem=1
перевод: http://euler.jakumo.org/problems/view/1.html

Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5
'''
# solved 07.05.2019 13:48 (233168)


sum=0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        sum+=i
        print(i, sum)