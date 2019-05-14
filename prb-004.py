# VSCraft
'''
задача:  https://projecteuler.net/problem=4
перевод: http://euler.jakumo.org/problems/view/4.html

Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
'''
# solved 07.05.2019 15:08 (906609)

def reverse(ss):
        list=[]
        for i in ss:
                list.append(i)
        list.reverse()
        return ''.join(list)

def is_poly(num):
        w = str(num)
        l = len(w)
        if not l%2==0:
                return False
        left = w[0:int(l/2)]
        righ = reverse(w[int(l/2):])
        if left == righ:
                return True
        return False
cnt=0
lst=[]
for i in range(999,100,-1):
        for k in range(999,100,-1):
                if cnt>10000:
                        break
                cnt+=1
                if is_poly(k*i):
                        lst.append(k*i)
                        print(k,'*',i,'=',k*i)
print(max(lst))
