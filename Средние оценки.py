import pandas
import seaborn

data = pandas.read_csv('support_data.csv')

# названия сегментов и интервалов
segments_old = ['Segment 0', 'Segment 1', 'Segment 2']
segments_new = ['Потенциальные клиенты', 'Обычные клиенты', 'VIP-клиенты']
intervals = ['До внедрения роботов', 'После внедрения роботов']

intervals_column = list(data['interval'])
segments_column = list(data['segment']) # ваш код здесь
score_column = list(data['score']) # ваш код здесь

# средние оценки
mean_scores = []

# ваш код здесь
for segment in segments_old:
    scores_do = 0
    scores_posle = 0
    sum_scores_do = 0
    sum_scores_posle = 0
   
    for index in range(len(data)):
        if segments_column[index] == segment:
            if intervals_column[index] == 'До внедрения роботов':
                scores_do += 1
                sum_scores_do += score_column[index]
            else:
                scores_posle += 1
                sum_scores_posle += score_column[index]
   
    segment_scores = [sum_scores_do / scores_do , sum_scores_posle / scores_posle ] # допишите код
    mean_scores.append(segment_scores) 

seaborn.heatmap(mean_scores, xticklabels=intervals, yticklabels=segments_new, annot=True, cmap='RdYlGn')