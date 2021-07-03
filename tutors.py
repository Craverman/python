from itertools import zip_longest
import itertools
tutors = [
    'Семен', 'Питер', 'Влад', 'Владиславиус',
    'Владик', 'Владислав', 'Елена', 'Владлен'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

names_gen = zip_longest(tutors, klasses)
print(type(names_gen))
for i in names_gen:
    print(i)










