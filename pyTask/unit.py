__author__ = "Arsentyeva N."


import math
import numpy as np

# Ввод значений
def inputList(n: int):
    """Ввод n значений"""
    lst = []
    for i in range(1, n + 1):
        a = float(input(f"a{i}: "))  # ввод значений a1,..an
        lst.append(a)
    return lst


# 136o задача
def _136o(lst: list):
    """Вычисление суммы выражения из задачи 136o"""
    s = 0
    for a in lst:
        s += math.sqrt(10 + a * a)
    return s


# 178 задача
def _178(lst: list):
     """Определение количества членов ak последовательности a1,...,an: являющихся квадратами четных чисел;"""
     k = 0
     for a in lst:
         if math.sqrt(a) % 2 == 0:
             k += 1
     return k



# 334 задача
def _334(n: int, m: int):
    """Вычисление суммы ряда из задачи 334в"""
    s = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s +=  (j-i+1)/(i+j)
    return s


# Создаем матрицу из нулей
def createZeroMatrix(n:int):
    """Создание матрицы размера n*n с нулями"""
    zeros_matrix = np.zeros((n, n))  # размер передаём как кортеж
    return zeros_matrix

# Создаем матрицу из случайных чисел
def createMatrix(n:int):
    """Создание матрицы размера n*n со случайными числа от -10 до 10"""
    matrix = np.random.uniform(low=-10.00, high=10.0, size=(n,n))  # размер передаём как кортеж
    return matrix

# Вывод матрицы
def printMatrix(matrix):
    for row in matrix:
        for x in row:
            print(f"{x:8.3f}", end="  ")
        print("")


def _675(matrix: np.ndarray, new_column: list, i:int):
    """Решение 675 задачи, вставка нового столбца в исходную матрицу"""
    # Вставка значений
    new_matrix = np.insert(matrix, i, new_column, axis=1)  # (исходный массив; список индексов, куда вставить; значения,
                                                           # которые вставляем; по какой оси вставляем (0 — строки,
                                                           #  1 — столбцы))
    return new_matrix

