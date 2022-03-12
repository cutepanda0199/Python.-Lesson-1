"""
Яндекс.Музыка¶
Сравнение Москвы и Петербурга окружено мифами. Например:

Москва — мегаполис, подчинённый жёсткому ритму рабочей недели;
Петербург — культурная столица, со своими вкусами.
На данных Яндекс.Музыки вы сравните поведение пользователей двух столиц.

Цель исследования — проверьте три гипотезы:

Активность пользователей зависит от дня недели. Причём в Москве и Петербурге это проявляется по-разному.
В понедельник утром в Москве преобладают одни жанры, а в Петербурге — другие. Так же и вечером пятницы преобладают разные жанры — в зависимости от города.
Москва и Петербург предпочитают разные жанры музыки. В Москве чаще слушают поп-музыку, в Петербурге — русский рэп.
Ход исследования

Данные о поведении пользователей вы получите из файла yandex_music_project.csv. О качестве данных ничего не известно. Поэтому перед проверкой гипотез понадобится обзор данных.

Вы проверите данные на ошибки и оцените их влияние на исследование. Затем, на этапе предобработки вы поищете возможность исправить самые критичные ошибки данных.

Таким образом, исследование пройдёт в три этапа:

Обзор данных.
Предобработка данных.
Проверка гипотез.
"""

# импорт библиотеки pandas
import pandas as pd

# чтение файла с данными и сохранение в df
df = pd.read_csv('/datasets/yandex_music_project.csv')
# получение первых 10 строк таблицы df
display(df.head(10))
# получение общей информации о данных в таблице df
df.info()
# перечень названий столбцов таблицы df
print(df.columns)
# переименование столбцов
df = df.rename(columns={'  userID':'user_id', 'Track':'track', '  City  ':'city', 'Day':'day'})
# проверка результатов - перечень названий столбцов
print(df.columns)
# подсчёт пропусков
print(df.isna().sum())

# перебор названий столбцов в цикле и замена пропущенных значений на 'unknown'
columns_to_replace = ['track', 'artist', 'genre']

for item in columns_to_replace:
    df[item] = df[item].fillna('unknown')
    
# подсчёт пропусков
print(df.isna().sum())

# подсчёт явных дубликатов
print(df.duplicated().sum())

# удаление явных дубликатов (с удалением старых индексов и формированием новых)
df = df.drop_duplicates().reset_index(drop=True)

# проверка на отсутствие дубликатов
print(df.duplicated().sum())

# Просмотр уникальных названий жанров
df_genre = df['genre']
df_genre = df_genre.sort_values()
print(df_genre.unique())

# Функция для замены неявных дубликатов
def replace_wrong_genres(wrong_values, correct_value):
    for wrong_value in wrong_values: # перебираем элементы списка wrong_values
        df['genre'] = df['genre'].replace(wrong_value, correct_value)  # заменяем каждое неправильное имя
        
# Устранение неявных дубликатов
duplicates = ['hip', 'hop', 'hip-hop']
name = 'hiphop'
replace_wrong_genres(duplicates, name)

# Проверка на неявные дубликаты
df_genre = df['genre']
df_genre = df_genre.sort_values()
print(df_genre.unique())

# Подсчёт прослушиваний в каждом городе
display(df.groupby('city').count())

# Подсчёт прослушиваний в каждый из трёх дней
display(df.groupby(['day', 'city']).count())

# <создание функции number_tracks()>
# Объявляется функция с двумя параметрами: day, city.
def number_tracks(day, city):
# В переменной track_list сохраняются те строки таблицы df, для которых 
# значение в столбце 'day' равно параметру day и одновременно значение
# в столбце 'city' равно параметру city (используйте последовательную фильтрацию
# с помощью логической индексации).
    track_list = df[df['day'] == day]
    track_list = track_list[track_list['city'] == city]
# В переменной track_list_count сохраняется число значений столбца 'user_id',
# рассчитанное методом count() для таблицы track_list.
    track_list_count = track_list['user_id'].count()
# Функция возвращает число - значение track_list_count.
    return track_list_count

# Функция для подсчёта прослушиваний для конкретного города и дня.
# С помощью последовательной фильтрации с логической индексацией она 
# сначала получит из исходной таблицы строки с нужным днём,
# затем из результата отфильтрует строки с нужным городом,
# методом count() посчитает количество значений в колонке user_id. 
# Это количество функция вернёт в качестве результата

# количество прослушиваний в Москве по понедельникам
number_tracks('Monday', 'Moscow')

# количество прослушиваний в Санкт-Петербурге по понедельникам
number_tracks('Monday', 'Saint-Petersburg')

# количество прослушиваний в Москве по средам
number_tracks('Wednesday', 'Moscow')

# количество прослушиваний в Санкт-Петербурге по средам
number_tracks('Wednesday', 'Saint-Petersburg')

# количество прослушиваний в Москве по пятницам
number_tracks('Friday', 'Moscow')

# количество прослушиваний в Санкт-Петербурге по пятницам
number_tracks('Friday', 'Saint-Petersburg')

# Таблица с результатами
columns = ['city', 'monday', 'wednesday', 'friday']
data = [['Moscow', 15740, 11056, 15945], ['Saint-Petersburg', 5614, 7003, 5895]]

df_city_day = pd.DataFrame(data = data, columns = columns)
display(df_city_day)

# получение таблицы moscow_general из тех строк таблицы df, 
# для которых значение в столбце 'city' равно 'Moscow'
moscow_general = df[df['city'] == 'Moscow']

# получение таблицы spb_general из тех строк таблицы df,
# для которых значение в столбце 'city' равно 'Saint-Petersburg'
spb_general = df[df['city'] == 'Saint-Petersburg']

# Объявление функции genre_weekday() с параметрами table, day, time1, time2
# которая возвращает информацию о самых популярных жанрах в указанный день в
# заданное время:
def genre_weekday(table, day, time1, time2):
# 1) в переменную genre_df сохраняются те строки переданного датафрейма table, для
#    которых одновременно:
#    - значение в столбце day равно значению аргумента day
#    - значение в столбце time больше значения аргумента time1
#    - значение в столбце time меньше значения аргумента time2
#    Используйте последовательную фильтрацию с помощью логической индексации.
    genre_df = table[table['day'] == day]
    genre_df = genre_df[genre_df['time'] > time1]
    genre_df = genre_df[genre_df['time'] < time2]
# 2) сгруппировать датафрейм genre_df по столбцу genre, взять один из его
#    столбцов и посчитать методом count() количество записей для каждого из
#    присутствующих жанров, получившийся Series записать в переменную
#    genre_df_count
    genre_df_count = genre_df.groupby('genre')['user_id'].count()

# 3) отсортировать genre_df_count по убыванию встречаемости и сохранить
#    в переменную genre_df_sorted
    genre_df_sorted = genre_df_count.sort_values(ascending = False)
# 4) вернуть Series из 10 первых значений genre_df_sorted, это будут топ-10
#    популярных жанров (в указанный день, в заданное время)
    return genre_df_sorted.head(10)

# вызов функции для утра понедельника в Москве (вместо df — таблица moscow_general)
# объекты, хранящие время, являются строками и сравниваются как строки
# пример вызова: genre_weekday(moscow_general, 'Monday', '07:00', '11:00')
genre_weekday(moscow_general, 'Monday', '07:00', '11:00')

# вызов функции для утра понедельника в Петербурге (вместо df — таблица spb_general)
genre_weekday(spb_general, 'Monday', '07:00', '11:00')

# вызов функции для вечера пятницы в Москве
genre_weekday(moscow_general, 'Friday', '17:00', '23:00')

# вызов функции для вечера пятницы в Петербурге
genre_weekday(spb_general, 'Friday', '17:00', '23:00')

# одной строкой: группировка таблицы moscow_general по столбцу 'genre', 
# подсчёт числа значений 'genre' в этой группировке методом count(), 
moscow_genres = moscow_general.groupby('genre')['genre'].count()
# сортировка получившегося Series в порядке убывания и сохранение в moscow_genres
moscow_genres = moscow_genres.sort_values(ascending = False)

# просмотр первых 10 строк moscow_genres
display(moscow_genres.head(10))

# одной строкой: группировка таблицы spb_general по столбцу 'genre', 
# подсчёт числа значений 'genre' в этой группировке методом count(), 
spb_genres = spb_general.groupby('genre')['genre'].count()
# сортировка получившегося Series в порядке убывания и сохранение в spb_genres
spb_genres = spb_genres.sort_values(ascending = False)

# просмотр первых 10 строк spb_genres
display(spb_genres.head(10))