from memory_profiler import profile
from random import sample


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


@profile(precision=10)
def myfunc():
    NUM = 1000
    eratosthenes(NUM)
    ranges(NUM)
    generators(NUM)

if __name__ == '__main__':
    myfunc()

"""

Для малых значений до 1000 видно что вариант создания массива через генератор
сжирает больше памяти чем варианты через решето эрастофена без него

Line #    Mem usage    Increment   Line Contents
================================================
    56  32.7734375000 MiB  32.7734375000 MiB   @profile(precision=10)
    57                             def myfunc():
    58  32.7734375000 MiB   0.0000000000 MiB       NUM = 1000
    59  32.7734375000 MiB   0.0000000000 MiB       eratosthenes(NUM)
    60  32.7734375000 MiB   0.0000000000 MiB       ranges(NUM)
    61  33.3554687500 MiB   0.5820312500 MiB       generators(NUM)


Для больших значений видно что самый лучший вариант это без решета так как
проходит меньше раз по массивам соответственно Garbage Collector чистит память
лучше

Line #    Mem usage    Increment   Line Contents
================================================
    56  32.8437500000 MiB  32.8437500000 MiB   @profile(precision=10)
    57                             def myfunc():
    58  32.8437500000 MiB   0.0000000000 MiB       NUM = 4000
    59  32.9570312500 MiB   0.1132812500 MiB       eratosthenes(NUM)
    60  32.9648437500 MiB   0.0078125000 MiB       ranges(NUM)


"""
