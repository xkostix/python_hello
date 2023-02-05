# дано число n, вычислить факториал n!= 1*2*...*N
# 0! = 1
# Решить, используя WHILE

n = int(input('Число n = '))
factorial = 1
count = 1

if n == 0:
    factorial = 1
else:
    while count <= n:
        factorial *= count
        count += 1

print(factorial)
