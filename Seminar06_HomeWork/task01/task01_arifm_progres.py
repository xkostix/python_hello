# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arifm_progres(first1, diff1, quantity1, progres1):
    an = progres1.append(first1)
    for n in range(1, quantity1):
        an = progres1[n-1] + diff1
        progres1.append(an)
    return progres1


first = int(input('Первое число: '))
diff = int(input('Разность: '))
quantity = int(input('Количество: '))
progres = []

print(arifm_progres(first, diff, quantity, progres))
