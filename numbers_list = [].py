numbers_list = []

# Вводим числа в список.
for i in range(5):
    number = int(input("введите число: "))
    numbers_list.append(number)

#Определяем максимум и минимум в нашем списке
print(f"исходный массив: {numbers_list}")
print(f"Максимум: {max(numbers_list)}")
print(f"Минимум: {min( numbers_list)}")

#Ищем сумму всех чисел списка
print(f"Сумма:  {sum(numbers_list)}")
