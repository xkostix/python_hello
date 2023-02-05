#  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#  Пример:
# - 6782 -> 23
# - 0,56 -> 11

import math


def summ_by_int(num):
    num = float(num)
    # Если число дробное, то умножаем на 10, пока не станет целым
    while (num / math.ceil(num)) != 1:  # округляем знаменатель в большую сторону, иначе может / 0
        # округляем, чтобы не было длинной дроби в float:
        num = round((num * 10), 8)
    summ = 0
    while num > 0:
        summ = summ + (num % 10)
        num //= 10
    return summ


def summ_by_str(string):
    string = string.replace('.', '')
    summ = 0
    for i in string:
        summ += int(i)
    return summ


number = input('Введите вещественное число: ')
if not number.replace('.', '', 1).isnumeric():
    print(number.isnumeric())
    exit('Ошибка: это не число.')
method = int(input('Решить методом чисел (1) или методом строк (2)? '))
if method == 1:
    print(f'Найдено методом чисел {summ_by_int(number)}')
elif method == 2:
    print(f'Найдено методом строк {summ_by_str(number)}')

# Вывод: парсить строки в Python проще, чем числа (?)
