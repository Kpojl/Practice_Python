import math

s = int(input("Введите длину стороны:"))
n = int(input("Введите количество сторон:"))
c = math.pi / n

sum = (n * s ** 2) / (4 * math.tan(c))


print("площадь правильного многоугольника:", sum)
  
