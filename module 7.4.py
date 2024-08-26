#use %
team1_num = 5
team2_num = 6
print('В команде Мастера кода участников: %s!' % team1_num)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
#use format
score_2 = 42
team1_time = 8015.2
print("Команда Волшебники данных решила задач: {}".format(score_2))
print("Волшебники данных решили задачи за {}".format(team1_time))
#use 'f'
score_1 = 40
print(f'Команды решили {score_1} и {score_2} задач')
def result(score_1: int, score_2: int):
    result = []
    if score_1 < score_2:
        result = 'Победа команды Мастера кода'
    elif score_1 > score_2:
        result = 'Победа командв Волшебники кода'
    else:
        result = 'Ничья'
    return result
challenge_result = result(40, 42)
print(f'Результат битвы: {challenge_result}')
tasks_total = 82
time_avg = 350.4
print(f' Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

