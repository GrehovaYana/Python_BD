var_list = list(input("Enter number set: "))
for n in range(1, len(var_list), 2):
    var_list[n - 1], var_list[n] = var_list[n], var_list[n - 1]
print(var_list)

