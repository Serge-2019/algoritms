from collections import namedtuple


class Enterprise(namedtuple('Enterprise', 'name q1 q2 q3 q4')):
    @property
    def total(self):
        return self.q1 + self.q2 + self.q3 + self.q4

    def __eq__(self, other):
        return self.total == other.total

    def __gt__(self, other):
        return self.total > other.total

    def __lt__(self, other):
        return self.total < other.total

    def __float__(self):
        return float(self.total)

    def __str__(self):
        return f'  {self.name}: avg = {self.total/4} total = {self.total}'

enterprises = []
while True:
    name = input('Введите имя предприятия [пусто для завершения]: ')
    if not name:
        break

    profits = []
    while len(profits) < 4:
        profits = input('  введите прибыль компании ' +
                        f'{name} за 4 квартала через пробел: ').split()
        try:
            profits = list(map(float, profits))
        except:
            profits = []
        profits = profits[0:4]
        if len(profits) < 4:
            print(' --- не верный ввод повторите ----')

    enterprises.append(Enterprise(name, *profits))

if not len(enterprises):
    print('Не введено ни одного предприятия')
else:
    print()
    # находим среднее как сумму всех сумм / кол-во предприятий
    avg = sum(map(float, enterprises)) / len(enterprises)
    print(f'Средняя прибыль по всем предприятиям = {avg:.2f}')

    # сортируем чтобы сверху были наименьшие числа
    enterprises.sort()
    i = 0

    # сначала выводим те кто меньше либо равен среднему
    print('Список предприятий чья прибыль НИЖЕ или равна среднему:')
    while i < len(enterprises) and enterprises[i].total <= avg:
        print(enterprises[i])
        i += 1

    # если чтото осталось то выводим те кто больше среднего
    if i < len(enterprises):
        print('Список предприятий чья прибыль ВЫШЕ среднего:')
        while i < len(enterprises):
            print(enterprises[i])
            i += 1
