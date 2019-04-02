import cProfile
from random import sample


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


def main():
    CNT = 20
    mas = [sample(range(100), CNT) for _ in range(CNT)]
    for _ in range(10000):
        max_func(mas, CNT)
    for _ in range(10000):
        max_zip(mas)


cProfile.run('main()')

"""
тоже самое видно по профайлеру

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.797    0.797 <string>:1(<module>)
       20    0.000    0.000    0.000    0.000 _collections_abc.py:302(__subclasshook__)
        6    0.000    0.000    0.000    0.000 _collections_abc.py:392(__subclasshook__)
       40    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
    26/21    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
      444    0.001    0.000    0.001    0.000 random.py:224(_randbelow)
       20    0.001    0.000    0.002    0.000 random.py:286(sample)

    10000    0.071    0.000    0.222    0.000 task1a.py:17(max_zip)

        1    0.010    0.010    0.797    0.797 task1a.py:27(main)
        1    0.000    0.000    0.002    0.002 task1a.py:29(<listcomp>)

    10000    0.563    0.000    0.563    0.000 task1a.py:5(max_func)

       40    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
    26/21    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        1    0.000    0.000    0.797    0.797 {built-in method builtins.exec}
       40    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
       20    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   200000    0.152    0.000    0.152    0.000 {built-in method builtins.min}
       20    0.000    0.000    0.000    0.000 {built-in method math.ceil}
       20    0.000    0.000    0.000    0.000 {built-in method math.log}
      400    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
      444    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      569    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

"""