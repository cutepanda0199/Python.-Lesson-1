import pandas as pd
df = pd.read_csv('music_log_upd.csv')

# <введите здесь решение для поиска недостающих данных>
#genre_rock = df[
    #(df['genre_name'] == 'rock')
    #& (df['total_play_seconds'] != 0)
#]
genre_rock = df[df['genre_name'] == 'rock']
genre_rock = genre_rock[genre_rock['total_play_seconds'] != 0]

# максимальное время прослушивания в жанре рок
genre_rock_max = genre_rock['total_play_seconds'].max()
print('Максимальное время прослушивания в жанре рок равно:', genre_rock_max)
# минимальное время прослушивания в жанре рок
genre_rock_min = genre_rock['total_play_seconds'].min()
print('Минимальное время прослушивания в жанре рок равно:', genre_rock_min)