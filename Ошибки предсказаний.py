Для первой стратегии:


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
years_numbers = list(range(1980, 2020))
    
# ваш код здесь
error_acres = []
for index in range(1, len(acres_usa)):
    error_acres.append(production_usa[index] - acres_usa[index] * yield_usa[index - 1] )

import seaborn
seaborn.barplot(x = years_numbers[1:], y = error_acres)





Для второй стратегии:


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
years_numbers = list(range(1980, 2020))
    
# ваш код здесь
error_yield = []
for index in range(1, len(acres_usa)):
    error_yield.append(production_usa[index] - acres_usa[index - 1] * yield_usa[index])
    
import seaborn
seaborn.barplot(x = years_numbers[1:], y = error_yield)