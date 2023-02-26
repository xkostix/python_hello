#  Вычислить число c заданной точностью d
#  Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# Вычисляем до 10 знаков.
# Берем метод Нилаканта:
# pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14) ...

d = int(input('Количество знаков после запятой: '))
# достаточ колич циклов для точности 'd':
number_of_cycles = (d * 2) * (d) * 10

pi = 3
even_cycle = False  # четный цикл (быстрее вычислить, чем i%2=0)
denominator_1 = 2  # первое число в знаменателе
i = 0

while i < number_of_cycles:
    denominator = denominator_1 * (denominator_1 + 1) * (denominator_1 + 2)
    if even_cycle:
        denominator *= -1
    pi = pi + 4 / denominator
    even_cycle = not even_cycle
    denominator_1 += 2
    i += 1

print(f'Рассчитано за {i} итераций:')
print(f'Сырые данные:      {pi}')
print(f'Заданная точность: {round(pi, d)}')
