"""
1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import hashlib
from random import randint

N = 10
k = 31
md = 1e9+7

# заполняем строку
s = "asndhyasnh"
# s = ""
# for _ in range(N):
#     s += chr(randint(ord('a'), ord('z')))
print(f'Исходная строка: "{s}"')

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
        print(f'{j}:{i}: {hsh:10} - {s[j:j+i]}', )
    i += 1

cnt = len(cnt)  # считаем кол-во хешей в сете
cnt += N  # отдельные буквы
print(f'Итоговое количество подстрок: {cnt}')
