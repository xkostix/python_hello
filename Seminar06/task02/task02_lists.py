# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых есть два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

def inputList(my_list):
    quantity = int(input(f'Количество элементов в массиве: '))
    print('Введите элементы массива, через Enter:')
    for i in range(quantity):
        my_list.append(int(input()))
    print()


def count_spec_elem(my_list):
    count_elem = 0
    for i in range(len_of_list1):
        if i not in (0, len_of_list1 - 1):
            if my_list[i-1] < my_list[i] and my_list[i+1] < my_list[i]:
                count_elem += 1
    return count_elem


list1 = []
inputList(list1)
len_of_list1 = len(list1)
print(count_spec_elem(list1))
