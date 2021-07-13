import json

with open("text_77.json", "w") as write_f:
    with open("text_7.txt", "r", encoding="utf-8") as f:
        profit_dict = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
        full_dict = [profit_dict, {"average_profit": sum([int(el) for el in profit_dict.values() if int(el) > 0]) / len(
            [int(el) for el in profit_dict.values() if int(el) > 0])}]
    json.dump(full_dict, write_f, ensure_ascii=False)
