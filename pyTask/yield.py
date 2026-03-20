__author__ = "Arsentyeva"

def factorials(n):
    '''Вывод факториала n!'''
    fact = 1
    for i in range(1,n+1):
        fact *= i
        yield fact


n = int(input("n! = "))

k = 1                                 # для запоминания числа n!
for x in factorials(n):
    print(f"{k}! =", x)
    k += 1

# test
assert list(factorials(1)) == [1]
assert list(factorials(6)) == [1,2,6,24,120,720]
assert list(factorials(0)) == []

