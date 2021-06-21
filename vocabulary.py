vocabulary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять',
              'Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten': 'Десять',
              'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
              'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate_adv(number):
    if number in vocabulary:
        return (vocabulary[number])
    else:
        print('none')

print(num_translate_adv('six'))

