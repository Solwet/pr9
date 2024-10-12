import random
numbers=[]
result=[]

def intinput(prompt):
    while True:
        try:
            Value = int(input(prompt))
            if Value > 0:
                return Value
            else:
                print("Ошибка: Введите положительное целое число.")
        except ValueError:
            print("Ошибка: Введите корректное целое число.")

count=intinput("Введите количество чисел в списке:")

for i in range(count):
    numbers.append(random.randint(-100,100))
print("Список до замены минимального и максимального элементов:", numbers)

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print("Список после замены минимального и максимального элементов:", numbers)
