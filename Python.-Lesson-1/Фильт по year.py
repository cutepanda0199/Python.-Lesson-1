import pandas

data = pandas.read_csv('crops_usa.csv')

# преобразуем Acres, Year и State в списки
acres = list(data['Acres'])
years = list(data['Year'])
states = list(data['State'])

# создайте новые списки
acres_2019 = []
states_2019 = []
# отфильтруйте значения в acres и states по значению в year
for index in range(len(data)):
    if years[index] == 2019:
        acres_2019.append(acres[index])
        states_2019.append(states[index])

print(acres_2019)
print(states_2019)