num_list = [5, 5, 5, 8, 8, 9, 3, 3, 3, 2]
new_list = [el for el in num_list if num_list.count(el) <2 ]

print(new_list)