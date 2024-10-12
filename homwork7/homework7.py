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
print("Список до циклического сдвига вправо:", numbers)

if len(numbers) > 1:
    last_element = numbers[-1]  
    for i in range(len(numbers) - 1, 0, -1): 
        numbers[i] = numbers[i - 1]
    numbers[0] = last_element

print("Список после циклического сдвига вправо:", numbers)