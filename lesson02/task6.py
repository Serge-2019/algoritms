from random import randint

num = randint(0, 100)

for i in range(10):
    try:
        tr = int(input('введите число: '))
    except:
        print('неверный ввод')
        continue

    if tr == num:
        break
    elif tr > num:
        print('ваше число БОЛЬШЕ загаданого')
    else:
        print('ваше число МЕНЬШЕ загаданого')

if tr == num:
    print('ВЫ УГАДАЛИ!')
else:
    print(f'вы не угадали число: {num}')
