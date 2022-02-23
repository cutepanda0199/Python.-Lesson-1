import pandas
data = pandas.read_csv('crops_usa.csv')

acres = list(data['Acres'])
years = list(data['Year'])

acres_usa = []

for year in range(1980, 2020):  # проходим по всем годам
    acres_one_year = []         # создаём список для одного года
    for index in range(len(data)):  # проходим по всем индексам датасета
        if years[index] == year:     # фильтруем значения acres за один год
            acres_one_year.append(acres[index])
    acres_usa.append(sum(acres_one_year))  # суммируем значения за один год
                                           # и добавляем результат в acres_usa

print('Общие площади за каждый год:', acres_usa)