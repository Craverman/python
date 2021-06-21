from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(number):
    """combine n jokes from patterns"""
    for i in range(number):
        jokes = choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives)
        print(jokes)

get_jokes(5)


