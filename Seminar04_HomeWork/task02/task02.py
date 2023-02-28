# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

n = int(input('Введите число: '))
temp_n = n
factor = 2  # множитель
factors_list = list()  # список простых множителей

while temp_n != 1:
    if temp_n % factor == 0:
        temp_n = temp_n / factor
        factors_list.append(factor)
    else:
        factor = factor + 1

print('Множители: ', end='')
print(*factors_list)
