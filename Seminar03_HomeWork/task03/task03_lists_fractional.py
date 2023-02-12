# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math

number_list = [1.1, 1.2, 3.1, 5, 10.01]

decimal_list = list()
i = 0

# Creating list of values "after the decimal point"
while i < len(number_list):
    dec_num = number_list[i] % (math.floor(number_list[i]))
    # Round because of Python Float problems:
    decimal_list.append(round(dec_num, 10))
    i += 1

print(f'Дробные части: {decimal_list}')

min_decimal = decimal_list[0]
max_decimal = 0
i = 0
while i < len(number_list):
    if decimal_list[i] < min_decimal:
        if decimal_list[i] != 0:
            min_decimal = decimal_list[i]
    if decimal_list[i] > max_decimal:
        max_decimal = decimal_list[i]
    i += 1

print(
    f'Разница между {max_decimal} и {min_decimal}: {round(max_decimal - min_decimal, 10)}')
