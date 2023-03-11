# Последовательностью Фибоначчи называется
# последовательность чисел a0 , a1 , ..., an , ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7   Output: 21
# Задание необходимо решать через рекурсию

def Fibonachi(n):
    if n < 2:
        return n
    return Fibonachi(n-1) + Fibonachi(n-2)


number = int(input())

if number == 0:
    fibo = 0
elif number == 1:
    fibo = 1
else:
    fibo = Fibonachi(number)

print(fibo)

# для больших чисел рекурсия - неоптимальна, долго работает, требует памяти.
# Для Фибоначчи оптимально - цикл:
# a = [1, 1]
# for i in range(2, 100):
#     a.append(a[i-1] + a[i-2])
