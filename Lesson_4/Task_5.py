from functools import reduce


def my_func(el_1, el_2):
    return el_1 * el_2


el = [el for el in range(100, 1000) if el % 2 == 0]
print(el)
print(reduce(my_func, el))
