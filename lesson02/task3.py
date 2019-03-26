num = ''
while not num.isnumeric():
    num = input('Введите натуральное число: ').strip()

rev = ''
for i in num:
    rev = i + rev

print(f'обратное число {rev}')
