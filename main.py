dict_sum = {}
dict_text = {}

with open('1.txt', 'r', encoding='utf-8') as f:
    name = '1.txt'
    sum_str = 0
    str_ = []
    for line in f:
        sum_str += 1
        str_.append(line)
        dict_text[name] = str_
    dict_sum.setdefault(name, sum_str)

with open('2.txt', 'r', encoding='utf-8') as f:
    name = '2.txt'
    sum_str = 0
    str_ = []
    for line in f:
        sum_str += 1
        str_.append(line)
        dict_text[name] = str_
    dict_sum.setdefault(name, sum_str)

with open('3.txt', 'r', encoding='utf-8') as f:
    name = '3.txt'
    sum_str = 0
    str_ = []
    for line in f:
        sum_str += 1
        str_.append(line)
        dict_text[name] = str_
    dict_sum.setdefault(name, sum_str)

import operator

sorted_dist = dict(sorted(dict_sum.items(), key=operator.itemgetter(1)))

with open("Texts.txt", "wt", encoding="utf=8") as new_file:
    for key, value in sorted_dist.items():
        new_file.write(key + '\n')
        new_file.write(str(value) + '\n')
        for new_line in dict_text[key]:
            new_file.write(new_line.strip() + '\n')
            new_line = new_line.strip()
            print(new_line)
