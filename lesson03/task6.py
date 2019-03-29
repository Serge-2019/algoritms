from random import sample

mas = sample(range(100), 10)

n = mas.index(min(mas))
m = mas.index(max(mas))
if n > m:
    n, m = m, n
part = mas[n+1:m]

print(f'Массив {mas}, min index: {n}, max index: {m}')
print(f'Часть массива {part}, cумма элементов: {sum(part)}')
