with open("text_3.txt", "r", encoding="utf-8") as emp_list:
    emp_dict = {line.split()[0]: float(line.split()[1]) for line in emp_list}
    print(f"Salary lower than 20000 = {[el[0] for el in emp_dict.items() if el[1] < 20000]}\n"
          f"Average salary: {sum(emp_dict.values()) / len(emp_dict)} ")
