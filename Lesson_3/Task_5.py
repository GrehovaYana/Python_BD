
def num_sum():
    summary = 0
    while True:
        print(f"Sum - {summary}")
        num_list = input('Enter list of number with shifts or quit - #: ').split()
        for num in num_list:
            if num == '#':
                print(f"Sum - {summary}")
                break
            try:
                summary += float(num)
            except ValueError:
                print("Something went wrong")
        else:
            continue
        break
    return f'Sum = {summary}'


num_sum()
