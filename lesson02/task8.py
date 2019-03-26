try:
    n = int(input('количество чисел: '))
    m = int(input('искомое число: '))
except:
    print('неверный ввод')
else:
    i = 0
    sm = 0
    while i < n:
        try:
            s = int(input(f'N{i+1}: '))
        except:
            print('неверный ввод')
        else:
            if s == m:
                sm += 1
            i += 1

    print(f'число {m} встретилось {sm} раз')
