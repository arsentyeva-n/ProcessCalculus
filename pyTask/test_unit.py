__author__ = "Arsentyeva"

import unit
import numpy as np

"""Модуль тестов к задачам 5-8"""

def test_136o():
    """Тест задачи 136o"""
    assert round(unit._136o([1,2,3,4,5]), 5) == 22.43228
    assert round(unit._136o([1000,-50000]), 5) == 51000.00510
    assert round(unit._136o([10.57, 3.3, -505.92]), 5) == 521.53334
    print("test_136o успешно пройден!")


def test_178():
    """Тест задачи 178в"""
    assert unit._178([2,3,25,4,49], 2) == 1
    assert unit._178([4,16,25,64,100], 5) == 2
    assert unit._178([9,81,121,99,33], 3) == 2
    print("test_178 успешно пройден!")


def test_334():
    """Тест задачи 334"""
    assert round(unit._334(3,4),5) == 4.06905
    assert round(unit._334(100,100),5) == 133.63396
    assert round(unit._334(2500,100),5) == -211902.90364
    print("test_334 успешно пройден!")


def test_675():
    """Тест задачи 675"""
    # 1 test
    matrix = unit.createZeroMatrix(6)
    new_column = np.array([[1, 2, 3, 4, 5, 6 ]])
    i = 5
    test_matrix = [[0,0,0,0,0,1,0],
                   [0,0,0,0,0,2,0],
                   [0,0,0,0,0,3,0],
                   [0,0,0,0,0,4,0],
                   [0,0,0,0,0,5,0],
                   [0,0,0,0,0,6,0]]
    result_matrix = unit._675(matrix, new_column, i)
    assert np.array_equal(test_matrix,result_matrix)

    #2 test
    matrix2 = unit.createZeroMatrix(4)
    new_column2 = np.array([[2.5, 1, -4, -1.1]])
    i2 = 0
    test_matrix2 = [[2.5, 0, 0, 0, 0],
                   [1, 0, 0, 0, 0],
                   [-4, 0, 0, 0, 0],
                   [-1.1, 0, 0, 0, 0]]
    result_matrix2 = unit._675(matrix2, new_column2, i2)
    assert np.array_equal(test_matrix2, result_matrix2)

    # 3 test
    matrix3 = unit.createZeroMatrix(3)
    new_column3 = np.array([[1, 1, 1]])
    i3 = 3
    test_matrix3 = [[0, 0, 0, 1],
                    [0, 0, 0, 1],
                    [0, 0, 0, 1]]
    result_matrix3 = unit._675(matrix3, new_column3, i3)
    assert np.array_equal(test_matrix3, result_matrix3)

    print("test_675 успешно пройден!")


test_136o()
test_178()
test_334()
test_675()