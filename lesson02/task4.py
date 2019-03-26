# возможно я не понял задания оно очень странно написано

try:
    n = int(input('Введите N: '))
except:
    print('Неверный ввод')
else:
    sm = 0
    row = 1
    while n > 0:
        sm += row
        row /= -2
        n -= 1

    print(f'Сумма: {sm}')
