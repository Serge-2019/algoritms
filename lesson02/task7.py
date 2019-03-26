try:
    n = int(input('введите число: '))
    nm = n * (n+1) / 2
except:
    print('неверный ввод')

sm = 0
while n > 0:
    sm += n
    n -= 1

print(f' n! = {sm}, n(n+1)/2 = {nm}')

if float(sm) == float(nm):
    print('доказано')
else:
    print('НЕ доказано')
