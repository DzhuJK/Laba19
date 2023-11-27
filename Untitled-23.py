import pandas as pd
f = open("input.csv", 'r', encoding='utf-8')
list1 = []
list2 = []
for lines in f:
    x = lines.index('')
    s1 = lines[0:x]
    s2_values = [int(value) for value in lines[(x+1):-1].split(', ')]
    s2 = sum(s2_values) 
    list1.append(s1)
    list2.append(s2)
f.close()
data = {'Фірма': list1, 'Кількість': list2}
df = pd.DataFrame(data)

total_tires = df.groupby('Фірма')['Кількість'].sum()

print(total_tires)
print(df)
