import random
numbers=[]

count=int(input("Введите количество чисел в списке:"))
for i in range(count):
    numbers.append(random.randint(-100,100))

print(numbers)
