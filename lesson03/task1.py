
sm = [0]*8

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            sm[j-2] += 1

for k, s in enumerate(sm):
    print(f'Число {k+2} кол-во: {s}')
