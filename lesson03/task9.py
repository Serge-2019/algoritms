from random import sample

mas = [sample(range(100), 10) for _ in range(10)]

m = -1
for i in range(10):
    n = 10000
    print(mas[i])
    for j in range(10):
        if mas[j][i] < n:
            n = mas[j][i]
    if n > m:
        m = n

print(f'Максимальный среди минимальных: {m}')

# второй способ
mx = -1
mas = zip(*mas)  # транспонируем матрицу
for row in mas:
    n = min(row)
    if n > mx:
        mx = n


print(f'(через ZIP) Максимальный среди минимальных: {mx}')
