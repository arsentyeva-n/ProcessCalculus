__author__ = "Arsentyeva"

import unit

# https://ivtipm.github.io/Programming/Glava07/index07.htm#z178

print(unit._178.__doc__) # вывод коментариев функции

n = int(input("Введите n: "))
x = int(input("Введите x, на которое делить: "))
lst = unit.inputList(n)  # ввод значений
k = unit._178(lst, x)    # вызов функции задачи 178

print(f"Количество чисел четных {x} = {k}")
