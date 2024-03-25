"""
� Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте процессы.
"""
import multiprocessing
import os
import time

MY_PATH = '.'


def worker(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f'Кол-во слов в файле <<{file}>> равно: {len(content.split())}')


if __name__ == '__main__':
    start_time = time.time()
    multiprocess = []

    for root, dirs, file_name in os.walk(MY_PATH):
        for f in file_name:
            t = multiprocessing.Process(target=worker, args=(f,))
            multiprocess.append(t)
            t.start()

    for t in multiprocess:
        t.join()

    print(f'Время выполнения: {(time.time() - start_time):.4f}')
