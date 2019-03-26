while True:

    try:
        a = int(input('первое число: ').strip())
        b = int(input('второе число: ').strip())
    except:
        print('Неверные данные')
        continue

    while True:
        znak = input('знак (0 - выход): ').strip()
        if znak not in ['0', '+', '-', '*', '/']:
            print('Знак неверный!')
            continue
        else:
            break

    if znak == '0':
        break

    res = None
    if znak == '+':
        res = a + b
    elif znak == '-':
        res = a - b
    elif znak == '*':
        res = a * b
    elif b == 0:
        print('На ноль делить нельзя')
        continue
    else:
        res = a / b

    print(f'{a} {znak} {b} = {res}')
