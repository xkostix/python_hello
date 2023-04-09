# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b-1)


a = int(input('Число: '))
b = int(input('Степень: '))
print(power(a, b))
