# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list_input = [1, 2, 3, 4, 5]
K = 3

# Вариант без использования .pop()
# N = len(list_input)
# for k in range(1, K+1):
#     last_number = list_input[-1]
#     i = 0
#     while i < (N - 1):
#         list_input[-i - 1] = list_input[-i - 2]
#         i += 1
#     list_input[0] = last_number

# вариант проще, с использованием pop()
for i in range(K):
    last_number = list_input.pop()  # Удаляем последний элемент
    list_input.insert(0, last_number)  # и вставляем его на первую позицию
    # list_input.insert(0, list_input.pop()) - еще компактнее

print(list_input)
