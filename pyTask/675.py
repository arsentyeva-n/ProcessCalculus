# 675. Даны действительные числа a1,...,an действительная квадратная матрица порядка n (n ≥ 6).
# Получить действительную матрицу размера n x (n+1), вставив в исходную матрицу между пятым и
# шестым столбцами новый столбец с элементами a1,...,an

__author__ = "Arsentyeva"

import unit
import numpy as np

n = int(input("Введите n: "))
i = int(input("Выберите место столбца i>=0 i<=n: "))

matrix = unit.createZeroMatrix(n)                             # создание матрицы из 0
#new_column = unit.inputList(n)                               # самостоятельынй ввод нового столбца
new_column = np.random.uniform(low=-10.00, high=10.0, size=n) # заполнение нового столбца случайными числами, uniform для типа float

print(new_column )                                            # вывод столбца

result_m = unit._675(matrix, new_column, i)                   # Вставляем новый столбец в матрицу
unit.printMatrix(result_m)                                    # вывод матрицы


n2 = int(input("Введите n: "))
i2 = int(input("Выберите место столбца i>=0 i<=n: "))
matrix2 = unit.createMatrix(n2)                                 # Создаем матрицу со случайными числами
new_column2 = np.random.uniform(low=-10.00, high=10.0, size=n2) # заполнение нового столбца случайными числами, uniform для типа float
print(new_column2)
result_m2 = unit._675(matrix2, new_column2, i2)                 # Вставляем новый столбец в новую матрицу
unit.printMatrix(result_m2)