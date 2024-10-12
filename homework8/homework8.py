import random

def create_bilet_list(rows, cols):
    bilet_list = []
    for _ in range(rows):
        sublist = [random.randint(1, 100) for _ in range(cols)]
        bilet_list.append(sublist)
    return bilet_list
def user_selection(bilet):
    user_numbers = []
    for i in range(len(bilet)):
        print("Строка", i + 1, ":", bilet[i])
        while True:
            try:
                choice = int(input("Выберите число из строки " + str(i + 1) + ": "))
                if choice in bilet[i]:
                    user_numbers.append(choice)
                    break
                else:
                    print("Ошибка: Выберите число из предложенного списка.")
            except ValueError:
                print("Ошибка: Введите корректное целое число.")
    return user_numbers

rows=5
cols=5

bilet = create_bilet_list(rows, cols)
print("Созданный список списков:")
for sublist in bilet:
    print(sublist)

user_numbers = user_selection(bilet)
random_numbers = [random.choice(bilet[i]) for i in range(rows)]

print("Ваш выбор:", user_numbers)
print("Случайный выбор программы:", random_numbers)

matches = set(user_numbers) & set(random_numbers)
print("Совпадения:", list(matches))
if len(matches) == 5:
    print("УРА!!! ПОБЕДА!!!")
else:
    print("Вы проиграли :(")