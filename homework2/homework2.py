import math

a = float(input("Введите начало границы поиска: "))
b = float(input("Введите конец границы поиска: "))

start = math.ceil(min(a, b))  
end = math.floor(max(a, b))
result=[]
for i in range(start,end):
    result.append(i**2)

print(result)


