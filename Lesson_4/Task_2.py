num_list = [200, 300, 5, 6, 4, 3, 11, 78, 4]
new_list = [num_list[el] for el in range(1, len(num_list)) if num_list[el] > num_list[el - 1]]

print(new_list)
