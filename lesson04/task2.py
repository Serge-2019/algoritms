import timeit

NUM = 18


def eratosthenes(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return list(filter(lambda x: x != 0, sieve))


def ranges(n):
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n+1, number):
                numbers[candidate-2] = 0
    return list(filter(lambda x: x != 0, numbers))


def generators(n):
    s = [x for x in range(2, n) if x not in [i for sub in [list(
        range(2 * j, n, j)) for j in range(2, n // 2)] for i in sub]]
    return s


res1 = eratosthenes(NUM)
res2 = ranges(NUM)
res3 = generators(NUM)

print(res1, res2, res3, sep='\n')

t1 = timeit.timeit("eratosthenes(NUM)",
                   setup="from __main__ import eratosthenes, NUM",
                   number=100000)
t2 = timeit.timeit("ranges(NUM)",
                   setup="from __main__ import ranges, NUM",
                   number=100000)
t3 = timeit.timeit("generators(NUM)",
                   setup="from __main__ import generators, NUM",
                   number=100000)


print(f'Решето = {t1}\nFOR/Range = {t2}\nГенераторы = {t3}\n')

"""

Можно сделать вывод что Решето работает примерно также как и без-решета :)
Но всеже на больших цифрах можно видеть что вариант без-решета чуть выигрывает

Также дополнительно проверил вариант с генераторами списков
и обнаружил что они очень медленные и время сильно вырастает в зависимости
от заанного числа

Для количества 10:

    Решето = 0.65416098
    FOR/Range = 0.56948698
    Генераторы = 3.0105710069999994

Для количества 15:

    Решето = 0.890424547
    FOR/Range = 0.793737212
    Генераторы = 7.4553067219999996

Для количества 20:

    Решето = 1.089224902
    FOR/Range = 1.079288394
    Генераторы = 17.507943332

Для количества 200:

    Решето = 8.984244622999999
    FOR/Range = 8.510825953000001
    Генераторы = не оценивался

------

Сложность алгоритмов:

eratosthenes(NUM)       - логарифмическая сложность
ranges(NUM)             - логарифмическая сложность
generators(NUM)         - квадратичная сложность

"""
