res = 0
mx = 0
while True:
    num = input('введите еще одно число (0 - чтобы закончить): ')
    if not num.isnumeric():
        print('неверный ввод')
        continue

    if int(num) == 0:
        break

    sm = 0
    for i in num:
        sm += int(i)

    if sm > mx:
        res = num
        mx = sm

print(f'Максимальная сумма: {mx} для числа {res}')
