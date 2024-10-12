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

for i in range(count-1):
    if numbers[i] < numbers[i+1]:
        result.append(numbers[i+1])

if len(result) == 0:
    result.append("Таких элементов не найдено")
print("Изначальный список",numbers,"Элементы которые больше предыдущего элемента",result)



