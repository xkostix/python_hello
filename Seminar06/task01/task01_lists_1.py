# Даны два массива чисел. Требуется вывести те элементы
# первого массива(в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива


def inputList(my_list, list_num):
    quantity = int(input(f'Количество элементов в массиве #{list_num}: '))
    print('Введите элементы массива, через Enter:')
    for i in range(quantity):
        my_list.append(int(input()))
    print()


list_1 = []
list_2 = []
inputList(list_1, 1)
inputList(list_2, 2)
print(list_1)  # To check content of list
print(list_2)  # To check content of list

list_2_set = set(list_2)  # Оптимизация, чтобы убрать повторения элементов
list_result = []
for i in list_1:
    if i not in list_2_set:
        list_result.append(i)


print()
print('Этих элементов нет во втором массиве:')
print(list_result)
