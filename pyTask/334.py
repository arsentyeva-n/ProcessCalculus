__author__ = "Arsentyeva"

import unit


print(unit._334.__doc__) # вывод коментариев функции
n = int(input("Введите n: "))
m = int(input("Введите m: "))
s = unit._334(n,m)    # вызов функции задачи 334

print(f"Сумма ряда = {s:.5f}")
