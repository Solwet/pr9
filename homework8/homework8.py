import random

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

def create_bilet_list(rows, cols):
    bilet_list = []
    for _ in range(rows):
        # Создание подсписка с случайными числами
        sublist = [random.randint(1, 100) for _ in range(cols)]
        bilet_list.append(sublist)
    return bilet_list

# Ввод количества строк и столбцов
rows = intinput("Введите количество строк: ")
cols = intinput("Введите количество столбцов: ")

# Создание и вывод двумерного списка
bilet = create_bilet_list(rows, cols)
print("Созданный список списков:")
for sublist in bilet:
    print(sublist)
