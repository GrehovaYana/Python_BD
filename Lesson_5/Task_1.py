# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые
# пользователем.Об окончании ввода данных свидетельствует пустая строка.
with open("text_1.txt", "w", encoding="utf-8") as new_f:
    while True:
        data = input("Enter random n or 'Enter' to stop: ")
        if not data:
            break
        print(data, file=new_f)



