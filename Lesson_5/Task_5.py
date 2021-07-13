def summary():
    try:
        with open('text_5.txt', 'w+') as f:
            line = input('Enter numbers with shifts \n')
            f.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Error in file')
    except ValueError:
        print('Wrong number')


summary()
