__author__ = "Arsentyeva"

"""
Реализовать функцию, которая будут выполнять HTTP запросы.
Синхронный код. Запросы выполняется последовательно/в цикле [в одном потоке], с единственным httpx.Client;
"""
# Синхронный (synchronous) режим — выполнение операций последовательно:
# когда одна операция вызывает другую и ждёт её завершения перед продолжением.
# То есть выполнение следующей операции блокируется до получения результата предыдущей.

import time
import httpx


def sync_task(client, url):
    """
    Принимает url сайта, отправляет запрос и получает ответ ( напр. статус 200 успешное соединение, 400 ошибка)
    """
    response = client.get(url)
    return response.status_code


def sync_main():
    """
    Главная синхронная функция
    """
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/users/1",
        "https://jsonplaceholder.typicode.com/todos",
        "https://jsonplaceholder.typicode.com/posts/1/comments",
        "https://jsonplaceholder.typicode.com/photos"
    ] * 3

    # Подключение через контекстный менеджер (как try\catch)
    with httpx.Client(timeout=10.0) as client:
        start_time = time.time()

        results = [sync_task(client, url) for url in urls]

        timer = time.time() - start_time
        #print("Результаты:", *results)
        # print(f"Все задачи выполнены за {timer:.2f} секунд")
        return timer


if __name__ == "__main__":
    sync_main()