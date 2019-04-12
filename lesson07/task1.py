"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы. Сортировка должна быть
реализована в виде функции. По возможности доработайте алгоритм (сделайте его
умнее).
"""
import timeit
from random import sample


def buble_sort(src):
    arr = src[:]
    ln = len(arr)-1
    for i in range(ln):
        for j in range(ln-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def buble_sort_enc(src):
    arr = src[:]
    ln = len(arr)-1
    while True:
        nln = 0
        for i in range(ln):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                nln = i
        ln = nln
        if ln < 1:
            break
    return arr


src = sample(range(-100, 100), 20)
print('Исходный массив:', src)

res = buble_sort(src)
print('Вариант 1 - итого:', res)
print('Время: ', timeit.timeit("buble_sort(src)",
                               setup="from __main__ import buble_sort, src",
                               number=20000))

res = buble_sort_enc(src)
print('Вариант 2 - итого:', res)
print('Время: ',
      timeit.timeit("buble_sort_enc(src)",
                    setup="from __main__ import buble_sort_enc, src",
                    number=20000))

"""
Вариант 1 - Время:  1.1101223489999998
Вариант 2 - Время:  0.86712532
"""
