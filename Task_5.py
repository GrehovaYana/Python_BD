my_list = [9, 8, 7, 7, 5, 3, 3, 1]
number = int(input("Enter new number: "))
i = 0
for el in my_list:
    if el >= number:
        i += 1
    else:
        break
my_list.insert(i, number)
print(my_list)
