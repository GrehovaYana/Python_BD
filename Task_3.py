seasons_list = [
    ['Winter', ['12', '1', '2']],
    ['Spring', ['3', '4', '5']],
    ['Summer', ['6', '7', '8']],
    ['Autumn', ['9', '10', '11']]
]

seasons_dict = {
    'Winter': ['12', '1', '2'],
    'Spring': ['3', '4', '5'],
    'Summer': ['6', '7', '8'],
    'Autumn': ['9', '10', '11']
}

month_number = input('Enter number of the month: ')
for season, months in seasons_list and seasons_dict.items():
    if month_number in months:
        print(f'{month_number} month of the year is {season}')
