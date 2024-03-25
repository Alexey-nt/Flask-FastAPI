"""
� Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте асинхронный подход.
"""
import asyncio
import os
import aiofiles
import time

MY_PATH = '.'


async def worker(file):
    async with aiofiles.open(file, 'r', encoding='utf-8') as f:
        content = await f.read()
        print(f'Кол-во слов в файле <<{file}>> равно: {len(content.split())}')


async def main():
    for root, dirs, file_name in os.walk(MY_PATH):
        for f in file_name:
            task = asyncio.create_task(worker(f))
            await task


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f'Время выполнения: {(time.time() - start_time):.4f}')
