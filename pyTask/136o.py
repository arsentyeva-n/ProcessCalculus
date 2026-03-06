__author__ = "Arsentyeva"
#https://ivtipm.github.io/Programming/Glava06/index06.htm#z136

import unit

print(unit._136o.__doc__) # вывод коментариев функции
print("Даны натуральное число n, действительные числа a1,..., an. Вычислить:")
n = int(input("Введите n: "))
lst = unit.inputList(n)  # ввод значений
s = unit._136o(lst)    # вызов функции задачи 136o

print(f"Сумма = {s:.5f}")
