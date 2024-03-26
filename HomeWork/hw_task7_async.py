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
import asyncio
from random import randint
import time


async def create_array():
    arr = []
    for i in range(10_000):
        arr.append(randint(1, 100))
    return arr


async def summa_array(start, stop):
    summa = 0
    for i in range(start, stop):
        summa += array[i]


array = create_array()


async def async_method():
    global array
    start_time = time.time()
    tasks = []
    for j in range(10):
        start_ = (j * len(array)) // 10
        finish_ = ((j + 1) * len(array)) // 10
        task = asyncio.create_task(summa_array(start_, finish_))
        tasks.append(task)
    await asyncio.gather(*task)
    print(f'Время выполнения равно: {(time.time() - start_time):.4f}')


    if __name__ == '__main__':
        asyncio.run(async_method())
