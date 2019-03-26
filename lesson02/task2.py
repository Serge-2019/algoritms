num = ''
while not num.isnumeric():
    num = input('Введите натуральное число: ').strip()

odd = 0
for i in num:
    if int(i) % 2 == 0:
        odd += 1

print(f'четных {odd}, нечетных {len(num)-odd}')
