#   Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 10)
# многочлена и записать в файл многочлен степени k.
#    Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input("Степень: "))
resultat = ''
coeff_list = list()

for i in reversed(range(k+1)):
    coeff = random.randrange(0, 11)
    if i != 0:
        if coeff != 0:
            if resultat != '':
                resultat += ' + '
            if coeff != 1:
                resultat += str(coeff) + '*'
            resultat += 'x'
            if i != 1:
                resultat += '^' + str(i)

    else:
        if coeff != 0:
            if resultat != '':
                resultat += ' + '
                resultat += str(coeff)

if resultat != '':
    resultat += ' = 0'
    print(resultat)
else:
    print('Попробуйте еще раз.')
