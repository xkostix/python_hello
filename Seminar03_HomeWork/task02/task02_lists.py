#   Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#   Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

input_list = input('Введите числа через пробел: ').split()

i = 0
while i < (len(input_list) / 2):
    print(int(input_list[i]) * int(input_list[-i-1]))
    i += 1
