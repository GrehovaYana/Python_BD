with open("text_1.txt", 'r', encoding="utf-8") as new_f:
    inf_ = [f"{line}. {len(count.split())} words" for line, count in enumerate(new_f, 1)]
    print(*inf_, f"{len(inf_)} strings", sep="\n")