def get_avg(scores):
    # sum=0
    # for score in scores:
    #     sum += score
    return sum(scores) / len(scores)

scores_school = [
    {'scores_class': '1', 'scores': [4,4,4]}, 
    {'scores_class': '2', 'scores': [5,5,5,]},
]

sum_scores = 0.0
for klass in scores_school:
    avg_per_class = get_avg(klass['scores'])
    sum_scores += avg_per_class
    print(f'Среднее по классу: {avg_per_class}')

avg_per_school = sum_scores / len(scores_school)    
print(f'Среднее по школе: {avg_per_school}')

     



