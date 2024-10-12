import math

def tryfloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
           
            print("Ошибка: Введите корректное число.")

a = tryfloat("Введите начало границы поиска: ")
b = tryfloat("Введите конец границы поиска: ")

start = math.floor(min(a, b))  
end = math.ceil(max(a, b))
result=[]
for i in range(start+1,end):
    result.append(i**2)

print(result)


