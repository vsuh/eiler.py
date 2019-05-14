# VSCraft
'''
задача:  https://projecteuler.net/problem=2
перевод: http://euler.jakumo.org/problems/view/2.html

Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.# solved
'''
# solved 07.05.2019 14:10 (4613733)

fb1 = 1
fb2 = 2
sum = fb2
i = 0
while True:
        i+=1
        fb = fb1+fb2
        if fb>4000000:
                break
        if fb%2==0:
                sum+=fb
        print('{}: {} ({})'.format(i, fb, sum))
        fb1 = fb2
        fb2 = fb
        
