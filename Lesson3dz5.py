#Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)

from random import choice, randrange
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def some_joke(n, repeat=False):
    """
    Функция делает случайные шутки из слов каждого списка
    :param n: колличество шуток
    :param repeat: уникальные/неуникальные
    :return:список случайных шуток

    """
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    list_of_joke = []
    list_min = min(no, adv, adj)

    while n and len(list_min):
        num = randrange(len(list_min))
        if repeat:
            list_of_joke.append(f"{no.pop(num)} {adv.pop(num)} {adj.pop(num)}")
        else:
            list_of_joke.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        n -= 1
    return list_of_joke
print(some_joke(10, True))



