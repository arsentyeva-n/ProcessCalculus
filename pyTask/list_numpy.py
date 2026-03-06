__author__="Arsentyeva N."

import random
import time
import numpy as np


def create_matrix(rows, cols):
    """Создание и заполнение матриц случайными числами"""
    return [[random.uniform(-10, 10) for i in range(cols)] for j in range(rows)]

def multi_matrix(matrix1, matrix2, result_matrix):
    """Перемножение 2-х матриц"""
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result_matrix



def create_matrix_np(rows, cols):
    """Создание и заполнение матриц случайными числами"""
    return np.random.uniform(-10, 11, size=(rows, cols))

def multi_matrix_np(matrix1, matrix2):
    """Перемножение 2-х матриц"""
    return np.dot(matrix1, matrix2)


# Создание двух случайных матриц list (правило количество столбцов матрицы1  = количеству строк матрицы2)
matrix1 = create_matrix(10, 10)
matrix2 = create_matrix(10, 10)

print("Первая матрица:")
for row in matrix1:
    print(row)

print("Вторая матрица:")
for row in matrix2:
    print(row)


result_matrix = [[0 for i in range(len(matrix2[0]))] for j in range(len(matrix1))] # создание матрицы с 0

# Засекаем время 
start_time = time.time()

result_matrix = multi_matrix(matrix1, matrix2, result_matrix) # вызов функции перемножения

end_time = time.time()

# Вычисляем время работы функции
result_time = (end_time - start_time) 
print(f"Время выполнения list: {result_time} секунд")


print("Результат умножения матриц:")
for row in result_matrix:
    print(row)


# Создание двух случайных матриц в numpy
matrix1 = create_matrix_np(10, 10)
matrix2 = create_matrix_np(10, 10)

# Засекаем время
start_time = time.time()

result_matrix = multi_matrix_np(matrix1, matrix2)  

end_time = time.time()

result_time = (end_time - start_time)
print(f"Время выполнения numpy: {result_time} секунд")

