#Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.

eng_rus_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}



def num_translate(eng_word):
    return eng_rus_dict.get(eng_word)

print(num_translate('one'))