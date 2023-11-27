import pandas as pd
import re

with open('laba.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
list1 = []
for line in lines:
    words = re.findall(r'\b\w+\b', line)
    list1.extend(words)

m = pd.Series(list1)
vowels = set(['a', 'e', 'i', 'o', 'u', 'y', 'а', 'е', 'и', 'о', 'у', 'і', 'ї', 'є', 'ю', 'я'])
k = m[m.apply(lambda x: len(x) >= 3 and sum(1 for letter in x.lower() if letter in vowels) >= 3)]
k.to_csv('laba1.txt', header=False, index=False)

print("Програма виконана успішно.")
