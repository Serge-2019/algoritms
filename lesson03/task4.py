from random import randint

mas = []
for _ in range(10):
    mas.append(randint(1, 10))

num = None
cnt = 0

for i in mas:
    k = mas.count(i)
    if k > cnt:
        cnt = k
        num = i

print(f'Массив {mas}, чаше всего встречается: {num}, в кол-ве: {cnt} раз')
