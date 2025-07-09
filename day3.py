import re

corrupted_data_string = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

def separate_by_dos(txt):
    pattern = r"don't|do"
    txt = re.split(pattern, corrupted_data_string)

    sorted_list = []
    counter = 0
    for i in txt:
        if (counter % 2) == 0:
            sorted_list.append(i)
        counter += 1
    return sorted_list

data_string = separate_by_dos(corrupted_data_string)

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
total = 0
for i in data_string:
    clean_data = re.findall(pattern, i)
    for x, y in clean_data:
        total += int(x) * int(y)

print(f'Total: {total}')