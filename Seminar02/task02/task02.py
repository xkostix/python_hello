# Дано число a > 0. Определить каким по счету оно в ряду Фибоначчи.
# Если не является числом из Фибоначчи, то вывести число -1.
# 1, 1, 2, 3, 5, 8, ...  (0 считаем нулевым по счету)

a = int(input('Введите число a: '))

if a == 0:
    print(f'Номер в ряду Фибоначчи = 0')
    exit()
elif a == 1:
    print(f'Номер в ряду Фибоначчи = 1 или = 2')
    exit()

fibonachi = 0
prev_number = 0
current_number = 1
counter = 1
is_in_fibonachi = -1
while fibonachi <= a:
    if a == fibonachi:
        is_in_fibonachi = 1
        break
    fibonachi = prev_number + current_number
    prev_number = current_number
    current_number = fibonachi
    counter += 1

if is_in_fibonachi == -1:
    print(f'-1.  (Число {a} не входит в ряд Фибоначчи)')
else:
    print(f'Номер в ряду Фибоначчи = {counter}')
