from datetime import datetime


def logger(path='my_log.log'):

    def __logger(old_function):

        def new_function(*args, **kwargs):

            file = open(f'{path}', 'a', encoding='utf8')
            file.write(f'{datetime.now()} '
                       f'Вызвылась функция: {old_function.__name__} '
                       f'с параметрами: {args} и {kwargs}\n')
            result = old_function(*args, **kwargs)
            file.write(f'Результатом вызова стало: {result}\n')
            file.close()
            return result

        return new_function

    return __logger
