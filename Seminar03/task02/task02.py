# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

my_list = [1, 1, 2, 0, -1, 1, 3, 4, 4]

# count_list = []

# for i in my_list:
#     if i not in count_list:
#         count_list.append(i)
# counter = len(count_list)


# вариант с использованием множества set():
counter = len(set(my_list))


print(f'Разных чисел: {counter}')
