# Example expert system

import numpy
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

score_table = numpy.array([0.0, 0.0])
questions = numpy.array(['Бывают ли у вас безпричинные приступы тревоги?', 'Вы перестали получать удовольствие от любимых вам действий?', 'Часто ли вы переживаете по мелочам?', 'Вас часто посещают мысли о бессмысленности жизни?', 'Вас посещают тревожные мыслм?', 'Ваше настроение портят сущие мелочи?'])
weight_table = numpy.array([[1.5, 0.0, 2.0, 0.0, 1.5, 0.0], [0.0, 1.5, 0.0, 2.0, 0.0, 1.5]])
results = numpy.array(['У вас есть характернык признаки тревожности, обратитесь к специалисту', 'У вас наблюдаются депресивные признаки, обратитесь к специалисту'])

for i in range(len(questions)):
    # print(Fore.YELLOW + f'i = {i}')
    print(f'{i+1}) ' + questions[i])
    answer = str(input())
    if answer == 'да':
        score_table[0] += weight_table[0][i]
        # print(f'+{weight_table[0][i]} TO score_table[0]')
    elif answer == 'нет':
        score_table[1] += weight_table[1][i]
        # print(f'+{weight_table[1][i]} TO score_table[1]')
    else:
        print(Fore.RED + 'Ошибка!')

# print(f'Тревожность = {score_table[0]}; Депрессивоность =  {score_table[1]}')

# Сравнивается сумма набранных баллов Т и Д
if score_table[0] > score_table[1]:
    print(results[0])
else:
    print(results[1])