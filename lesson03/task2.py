from random import sample

mas = sample(range(100), 10)
res = []
for i in range(len(mas)):
    if mas[i] % 2 == 0:
        res.append(i)

print(f'Массив {mas}\nИндексы {res}')
