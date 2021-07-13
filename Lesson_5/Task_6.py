import string

with open("text_6.txt", "r", encoding="utf-8") as final_dict:
    final_marks = {string.split(":")[0]: sum([int(s[:s.index("(")]) for s in string.split() if "(" in s]) for string in
                   final_dict}
    print(final_marks)
