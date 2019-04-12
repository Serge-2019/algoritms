"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
from random import sample


def merge_sort(arr):
    if len(arr) <= 1:
        return False

    mid = len(arr)//2
    lft = arr[:mid]
    rgt = arr[mid:]

    merge_sort(lft)
    merge_sort(rgt)

    i = 0
    j = 0
    k = 0
    while i < len(lft) and j < len(rgt):
        if lft[i] > rgt[j]:
            arr[k] = lft[i]
            i += 1
        else:
            arr[k] = rgt[j]
            j += 1
        k += 1

    while i < len(lft):
        arr[k] = lft[i]
        i += 1
        k += 1

    while j < len(rgt):
        arr[k] = rgt[j]
        j += 1
        k += 1


src = sample(range(0, 100), 20)
print('Исходный массив:', src)

merge_sort(src)
print('Результат:', src)
