__author__ = "Arsentyeva"

"""
Реализовать функцию, которая будут выполнять HTTP запросы.
Асинхронный код. Запросы выполняются в одном потоке, используя asyncio + httpx.AsyncClient и asyncio.create_task / gather.
"""

# Асинхронный (asynchronous) режим — выполнение операций организовано так,
# что одна задача может инициировать другую и не ждать её завершения — продолжать работать дальше.
# Результат другой операции приходит позже и обрабатывается отдельно:
# через функцию обратного вызова (callback), await, событие и т.д.).

import asyncio
import httpx
import time



async def async_task(client,url):
    """
    Принимает url сайта, отправляет запрос и получает ответ ( напр. статус 200 успешное соединение, 400 ошибка)
    """
    response = await client.get(url)
    return response.status_code


async def async_main():
    """
    Главная асинхронная функция
    """
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/users/1",
        "https://jsonplaceholder.typicode.com/todos",
        "https://jsonplaceholder.typicode.com/posts/1/comments",
        "https://jsonplaceholder.typicode.com/photos"
           ] * 3 # для больших запросов

    # Подключение через контекстный менеджер (как try\catch)
    async with httpx.AsyncClient(timeout=10.0) as client:
        start_time = time.time()
        # Добавление задач в очередь задач (event loop)
        tasks = [asyncio.create_task(async_task(client, url)) for url in urls]
        # Параллельное выполнение нескольких задач, в данном случае запросов
        results = await asyncio.gather(*tasks)
        timer = time.time() - start_time

        #print("Результаты:", *results)
        # #print(f"\nВсе задачи выполнены за {timer:.2f} секунд")
        return timer


if __name__ == "__main__":
    asyncio.run(async_main())



