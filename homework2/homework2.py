import math

a = float(input("Введите начало границы поиска: "))
b = float(input("Введите конец границы поиска: "))

start = math.ceil(min(a, b))  
end = math.floor(max(a, b))

print(start,end)


