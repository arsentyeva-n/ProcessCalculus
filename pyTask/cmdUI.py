__author__ = "Arsentyeva"
"""cmd arguments, pattern matching"""

import sys
import math

def main():
   # print(sys.argv) # выводим все аргументы
    args = sys.argv[1:] # получаем аргументы пользователя и обрезаем 1 аргумент (имя исполняемого файла)

    # pattern matching (сопоставление с образцом|шаблоном)
    match args:
        case []:
            print("Программа запущена без аргументов")
        case "sum", *other:                           # пример использования: python3 cmdUI.py 1 2 3
            num = [float(x) for x in other]
            print(f"Сумма: {sum(num)}")
        case ["prod", *other]:
            num = [float(x) for x in other]
            print(f"Произведение: {math.prod(num)}")
        case "--help",: #  todo
            print("Справка:")
            print("sum n1 n2 n3 ... - сумма чисел")
            print("prod n1 n2 n3 ... - произведение чисел")
        case _: # любое значение
            print("Неизвестная команда")


if __name__ == "__main__":
    main()


