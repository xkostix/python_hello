def funct(*args, **kwargs):
    print(args)  # кортеж (1,2,3,4,5)
    a, *b, c = args
    print(a, c)  # аргументы первый и последний: 1, 5
    print(b)  # все остальные аргументы, список: [2, 3, 4]
    print(kwargs)  # именованные арг - Словарь {}
    return 0


n = funct(1, 2, 3, 4, 5, name='Vasya', name_1='second')
