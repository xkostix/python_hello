li1 = [i for i in range(10)]  # список чисел от 0 до 10
print(li1)

li2 = [i for i in range(20) if i % 2 == 0]  # условие: четные числа
print(li2)

li3 = [i for i in li2 if i % 3 == 0]  # из другого списка с условием
print(li3)

# Dict_comprehension:
myDict = {i: i**2 for i in range(10)}  # число и его 2 степень
print(myDict)
