__author__ = "Arsentyeva"

import time


# sync
def sync_task(task_name, duration):
    print(f"Начинаю задачу: {task_name} (займет {duration} сек)")
    time.sleep(duration)  # Блокирующее ожидание
    print(f"Завершил задачу: {task_name}")
    return f"Результат {task_name}"


def sync_main():
    start_time = time.time()

    # Задачи выполняются одна за другой
    result1 = sync_task("Загрузка данных", 2)
    result2 = sync_task("Обработка данных", 1)
    result3 = sync_task("Сохранение результата", 1.5)

    timer = time.time() - start_time
    print(f"\nВсе задачи выполнены за {timer:.2f} секунд")
    print(f"Результаты: {result1}, {result2}, {result3}")


if __name__ == "__main__":
    sync_main()