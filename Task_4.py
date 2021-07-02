random_words = input("Enter random words with shift: ")
for ind, el in enumerate(random_words.split(), 1):
    print(ind, el[:10:])
