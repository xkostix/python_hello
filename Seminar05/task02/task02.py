# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def change(a):
    new_list = a.copy()  # если не хотим менять исходный список
    min_ = min(new_list)
    max_ = max(new_list)
    for i in range(len(new_list)):
        if new_list[i] == max_:
            new_list[i] = min_
    return new_list


a = [1, 3, 3, 3, 4]
print(a)
print(change(a))
