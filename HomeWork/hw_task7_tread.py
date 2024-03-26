"""
� Напишите программу на Python, которая будет находить
  сумму элементов массива из 10_000 целых чисел.
� Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
� Массив должен быть заполнен случайными целыми числами от 1 до 100.
� При решении задачи нужно использовать многопоточность,
                                        многопроцессорность
                                        и асинхронность.
� В каждом решении нужно вывести время выполнения вычислений.
"""
import threading
from random import randint
import time


def create_array():
    arr = []
    for i in range(10_000):
        arr.append(randint(1, 100))
    return arr


def summa_array(start, stop):
    summa = 0
    for i in range(start, stop):
        summa += array[i]


start_time = time.time()
threads = []
array = create_array()

for j in range(10):
    start = (j * len(array)) // 10
    finish = ((j + 1) * len(array)) // 10
    t = threading.Thread(target=summa_array, args=(start, finish))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print(f'Время выполнения  равно: {(time.time() - start_time):.4f}')
