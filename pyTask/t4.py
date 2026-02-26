__author__ = "Arsentyeva"

# Циклы

try:
    n = int(input("Введите неотрицательное целое число n: "))

    if n < 0:
        print("n должно быть неотрицательным")
    else:
        s = 0
        for i in range(1, n + 1):
            s = s + 1 / (2 * i) ** 2

        print(s)

except ValueError:
    print("введите целое число")