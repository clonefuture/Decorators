import datetime
import os


def log_deco(part_file):
    def part_deco(some_func):
        def new_func(*args, **kwargs):
            time_log = datetime.datetime.now()
            result = some_func(*args, **kwargs)
            with open(os.path.join(part_file, 'log_file.txt'), 'a', encoding='utf-8') as f:
                print(f'{time_log}\n'
                      f'вызвана функция {some_func.__name__} с аргументами {args} и {kwargs}\n'
                      f'результат выполнения функции - {result}\n'
                      f'{"-" * 60}\n', file=f)
            return result

        return new_func

    return part_deco


if __name__ == '__main__':

    path_to_log = r'C:\Users\user\Documents\Python\netology\decorators'

    @log_deco(path_to_log)
    def summarize(a, b):
        return a + b
    summarize(53, 22)
