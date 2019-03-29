from random import randint

mas = []
for _ in range(10):
    mas.append(randint(0, 40))

print(f'Массив {mas}')

n1 = mas.index(min(mas))
e1 = mas.pop(n1)
n2 = mas.index(min(mas))
e2 = mas.pop(n2)

print(f'min1 = {e1}, min2 = {e2}')
