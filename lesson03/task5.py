from random import sample

mas = sample(range(-50, 20), 20)

num = min(mas)
for i in mas:
    if i < 0 and i > num:
        num = i

print(f'Массив {mas}')
if num >= 0:
    print('Нет отрицательных чисел')
else:
    print(f'Максимальное отрицательное число: {num}')
