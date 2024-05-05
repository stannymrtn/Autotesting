import math
def square(x):
    print("Площадь квадрата=", x*x)

x = float(input("Введите сторону квадрата: "))
y = math.ceil(x)
square(y)
