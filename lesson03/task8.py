res = []
for i in range(4):
    while True:
        s = input(f'Введите 4 числа через пробел для {i} строки: ').split()
        try:
            s = list(map(int, s))
        except:
            print('неверный ввод')
        else:
            if len(s) != 4:
                print('количество чисел должно быть 4')
            else:
                break
    s.append(sum(s))
    res.append(s)

for i in res:
    print(i)
