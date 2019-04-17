"""
1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import timeit
import hashlib
from random import randint


# заполняем строку
s = "asndhyasnh"
# s = ""
# for _ in range(N):
#     s += chr(randint(ord('a'), ord('z')))
print(f'Исходная строка: "{s}"')


def my_count(s, debug=True):
    N = 10
    k = 31
    md = 1e9+7

    # считаем все степени p
    p = [1]
    for i in range(1, N):
        p.append(int(p[i-1] * k % md))

    # считаем значение хэш-функции для каждого префикса
    h = [0]
    for i in range(0, N):
        x = ord(s[i]) - ord('a') + 1
        h.append(int((h[i] + p[i] * x) % md))

    # функция для быстрого подсчета хеша любой подстроки
    def shash(l, r):
        return int((h[r] - h[l]) * p[N-1-l] % md)

    # перебор всех подстрок и добавление хешей в set
    i = 2
    cnt = set()
    while i < N:
        for j in range(N+1-i):
            hsh = shash(j, j+i)
            cnt.add(hsh)
            if debug:
                print(f'{j}:{i}: {hsh:10} - {s[j:j+i]}', )
        i += 1

    cnt = len(cnt) + 1  # считаем кол-во хешей в сете
    cnt += N  # отдельные буквы
    return cnt


def count_substring_hash(s: str):
    set_hash = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            set_hash.add(hash(s[i:j]))
            # print(s[i:j])
    return len(set_hash) - 1  # вычитаем совпадение строки с самой собой


def count_substring_sha1(s: str):
    set_sha1 = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            set_sha1.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
    return len(set_sha1) - 1


count_0 = my_count(s)
print(f'В строке "{s}" есть {count_0} различных подстрок')

count_1 = count_substring_hash(s)
print(f'В строке "{s}" есть {count_1} различных подстрок')

count_2 = count_substring_sha1(s)
print(f'В строке "{s}" есть {count_2} различных подстрок')


print(timeit.timeit('my_count(s, False)',
                    number=100000, globals=globals()))
print(timeit.timeit('count_substring_hash(s)',
                    number=100000, globals=globals()))
print(timeit.timeit('count_substring_sha1(s)',
                    number=100000, globals=globals()))
