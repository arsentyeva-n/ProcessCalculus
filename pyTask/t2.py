__author__="Arsentyeva N."

# Даны действительные числа x, y (x не равно y). Меньшее из этих двух чисел заменить их полусуммой, а большее - их удвоенным произведением.

x = float(input("Введите число x "))
y = float(input("Введите число y "))

sum = (x + y) / 2
prod = 2 * x * y

if x < y:
  x = sum
  y = prod
elif x > y:
  x = prod
  y = sum
else:
    print("x = y")


print(f"x = {x:1f}")
print(f"y = {y:1f}")