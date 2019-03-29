from random import sample

mas = sample(range(100), 10)

n = mas.index(min(mas))
m = mas.index(max(mas))

print(f'Массив {mas}, min: {mas[n]}, max: {mas[m]}')

mas[n], mas[m] = mas[m], mas[n]

print(f'изменненый массив: {mas}')
