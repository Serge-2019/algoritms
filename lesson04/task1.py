import timeit

from random import sample
CNT = 20
mas = [sample(range(100), CNT) for _ in range(CNT)]


def max_func(mas, cnt):
    m = -1
    for i in range(cnt):
        n = 10000
        for j in range(cnt):
            if mas[j][i] < n:
                n = mas[j][i]
        if n > m:
            m = n
    return m


def max_zip(mas):
    mx = -1
    res = zip(*mas)  # транспонируем матрицу
    for row in res:
        n = min(row)
        if n > mx:
            mx = n
    return mx


fn = timeit.timeit("max_func(mas, CNT)",
                   setup="from __main__ import max_func, mas, CNT",
                   number=100000)
zp = timeit.timeit("max_zip(mas)",
                   setup="from __main__ import max_zip, mas",
                   number=100000)

print(f'Через for: {fn}\nЧерез zip: {zp}')

"""

Можно сделать вывод что внутренняя функция ZIP + поиск потом через min по
строке будет работать практически всегда в 2 раза быстрее чем перебор через for

Для количества 10:

    Через for: 2.092409354
    Через zip: 0.7065722610000003

Для количества 15:

    Через for: 3.318680713
    Через zip: 1.227757919

Для количества 20:

    Через for: 5.164637806
    Через zip: 2.6922413329999992

Для количества 50:

    Через for: 27.386202571
    Через zip: 10.219514612000001

-----------

Сложность алгоритмов:

for         - квадратичная сложность?
zip         - линейная сложность?

"""
