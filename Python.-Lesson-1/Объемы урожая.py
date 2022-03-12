Первая стратегия:

import pandas
data = pandas.read_csv('crops_usa.csv')

acres = list(data['Acres'])
production = list(data['Production'])
years = list(data['Year'])

acres_usa = []
production_usa = []

for year in range(1980, 2020):
    acres_one_year = []
    production_one_year = []
    for index in range(len(data)):
        if years[index] == year:
            acres_one_year.append(acres[index])
            production_one_year.append(production[index])
    acres_usa.append(sum(acres_one_year))
    production_usa.append(sum(production_one_year))

yield_usa = []

for index in range(len(production_usa)):
    yield_usa.append(production_usa[index] / acres_usa[index])

# ваш код здесь
predict_acres = []
for index in range(1, len(acres_usa)):
    predict_acres.append(acres_usa[index] * yield_usa[index -1])

print(predict_acres)


Вторая стратегия:

import pandas
data = pandas.read_csv('crops_usa.csv')

acres = list(data['Acres'])
production = list(data['Production'])
years = list(data['Year'])

acres_usa = []
production_usa = []

for year in range(1980, 2020):
    acres_one_year = []
    production_one_year = []
    for index in range(len(data)):
        if years[index] == year:
            acres_one_year.append(acres[index])
            production_one_year.append(production[index])
    acres_usa.append(sum(acres_one_year))
    production_usa.append(sum(production_one_year))

yield_usa = []

for index in range(len(production_usa)):
    yield_usa.append(production_usa[index] / acres_usa[index])
    
predict_acres = []

for index in range(1, len(acres_usa)):
    predict_acres.append(acres_usa[index] * yield_usa[index - 1])
    
# ваш код здесь
predict_yield = []
for index in range(1, len(production_usa)):
    predict_yield.append(yield_usa[index] * acres_usa[index -1])
    
print(predict_acres)
print(predict_yield)