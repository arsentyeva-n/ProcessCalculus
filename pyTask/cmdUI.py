import sys          # для работы с аргументами командной строки
import math

def main():
    print(sys.argv) # выводим все аргументы
    args = sys.argv[1:] # получаем аргументы пользователя и обрезаем 1 аргумент (имя файла)

    match args:
        case []:
            print("Программа запущена без аргументов")
        case ["sum", *other]:
            num = [float(x) for x in other]
            print(f"Сумма: {sum(num)}")
        case ["multy", *other]:
            num = [float(x) for x in other]
            print(f"Произведение: {math.prod(num)}")


if __name__ == "__main__":
    main()



