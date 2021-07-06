def int_func():
    for latin_word in input("Enter set of latin words (lower case):\n ").split():
        elements = 0
        for element in latin_word:
            if 97 <= ord(element) <= 122:
                elements += 1
        print(latin_word.title() if elements == len(latin_word) else f"Use lower case!")


int_func()
