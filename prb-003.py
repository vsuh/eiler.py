# VSCraft
'''
задача:  https://projecteuler.net/problem=3
перевод: http://euler.jakumo.org/problems/view/3.html

Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
'''
# solved 07.05.2019 14:27 (6857)
import math


org=600851475143

def simp(num):
        nn = math.ceil(math.sqrt(num))
        list = []
        for ii in range(3, nn):
                if num%ii==0:
                        if simp(ii)==[]:
                                list.append(ii)
        return list

arr = simp(org)
print(max(arr))