from salary import calculate_salary
from people import get_employees
from datetime import datetime

if __name__ == '__main__':
    dattebayo = datetime.now()
    while True:
        a = input('Что сделать?\n'
                '1 - calculate_salary\n'
                '2 - get_employees\n'
                '3 - exit\n')
        if a == '1':
            print(dattebayo)
            calculate_salary()
        elif a == '2':
            print(dattebayo)
            get_employees()
        elif a == '3':
            break
        else:
            print('Вы ввели какой-то бред\n'
                  'Попробуй      ещё      раз :-)')
