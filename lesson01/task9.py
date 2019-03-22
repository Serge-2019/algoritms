# 9. Вводятся три разных числа. Найти, какое из них является
# средним(больше одного, но меньше другого).

try:
    a, b, c = input('Введите три числа a,b,c: ').split(',')
    a, b, c = (int(a), int(b), int(c))
except:
    print('Неверный ввод')
else:
    if a > b > c or c > b > a:
        print(f'Среднее: {b}')
    elif b > a > c or c > a > b:
        print(f'Среднее: {a}')
    else:
        print(f'Среднее: {c}')
