import math

def calculate(x, y, m):
    return ((x ** 3 + math.pi ** 2) ** (1/2)) + (math.e ** (y + 1)) + ((m + math.tan(m)) ** (1/2))

x = float(input("Введіть x -> "))
y = float(input("Введіть y -> "))
m = float(input("Введіть m -> "))

z = calculate(x, y, m)
print(z)