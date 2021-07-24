class OnlyIntErr:
    def __init__(self, *args):
        self.data = []

    def data_input(self):
        while True:
            try:
                val = int(input('Enter numeric values and press Enter - '))
                self.data.append(val)
                print(f'List - {self.data} \n ')
            except:
                print(f"String-invalid value")
                y_or_n = input(f'Try again? Y/N ')

                if y_or_n == 'Y':
                    print(list_.my_input())
                elif y_or_n == 'N':
                    return f'End'
                else:
                    return f'End'
                pass


list_ = OnlyIntErr(1)
print(list_.data_input())
