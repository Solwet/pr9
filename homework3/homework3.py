numbers = []
result=[]

while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    
    if user_input.lower() == 'end':
        break
    
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Ошибка: Введите корректное целое число.")

for i in range(len(numbers)):
    if numbers[i]%2 != 0:
        result.append(numbers[i])

if numbers:
    print("Нечетные числа:", result)
else:
    print("В списке нет нечетных чисел.")
