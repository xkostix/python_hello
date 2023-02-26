my_dict = {'cat': 'кошка', 'dog': 'собака', 'good': 'хороший'}
for key in my_dict:
    print(key, my_dict[key])

my_list = list(my_dict.items())
print(my_list)

print(my_list[1][1])  # index 1 (item 1) and second index 1 (elem in item 1)
