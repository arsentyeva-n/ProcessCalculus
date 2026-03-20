__author__ = "Arsentyeva"

import asyncio
import time


# async
async def async_task(task_name, duration):
    print(f"Начало обработки --- {task_name}")
    await asyncio.sleep(duration)  # Не блокирующее ожидание
    # имитация долгой I / O операции
    # await означает, что в этом месте корутина приостанавливается и даёт возможность выполнять другим корутинам,
    # до момента когда sleep не закончится
    print(f"Выполнено --- {task_name}")
    return f"{task_name}"


async def async_main():
    start_time = time.time()

    # задачи
    task1 = asyncio.create_task(async_task("Обработка данных", 3))
    task2 = asyncio.create_task(async_task("Отправление запроса",1))

    # Параллельное выполнение двух задач
    results = await asyncio.gather(task1, task2)
    print("Результаты:", *results)


    timer = time.time() - start_time
    print(f"\nВсе задачи выполнены за {timer:.2f} секунд")


if __name__ == "__main__":
    asyncio.run(async_main())