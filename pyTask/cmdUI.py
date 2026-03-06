import sys


def main():
    print(sys.argv)
    args = sys.argv[1:]

    match args:
        case []:
            print("программа запущена без аргументов")
        case [prod, *other]:
            num = [float(x) for i in other]
            print(f"Произведение: {prod(num)}")


if __name__ == "__main__":
    main()