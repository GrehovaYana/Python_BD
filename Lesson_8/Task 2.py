class DivisionErr(Exception):
    def __init__(self, txt):
        self.txt = txt


num_1 = input("Enter dividend num: ")
num_2 = input("Enter divider num: ")

try:
    div_res = int(num_1) // int(num_2)
    if num_2 == 0:
        raise DivisionErr("Division by zero is not allowed!")
except (ValueError, DivisionErr) as error:
    print(error)
else:
    print(round(div_res))
