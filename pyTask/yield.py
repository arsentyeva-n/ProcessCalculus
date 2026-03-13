__author__ = "Arsentyeva"

def degree(i):
    yield i*i

def factorials(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
        yield fact

n = int(input())
for i in range(1,n+1):
    print(f"b{i} =",next(degree(i)))

k = 1
for x in factorials(n):
    print(f"{k}! =", x)
    k += 1


assert list(degree(1)) == [1]
assert list(degree(2)) == [1,4]

assert list(factorials(1)) == [1]
assert list(factorials(6)) == [1,2,6,24,120,720]
