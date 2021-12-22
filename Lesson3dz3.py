#Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

def thesaurus(*args):
    name_list = {}
    for i in sorted(args):
        letter = i[0]
        if letter in name_list:
            name_list[letter] += [i]
        else:
            name_list[letter] = [i]

    return name_list

print(thesaurus("Иван", "Владислав", "Максим", "Алиса", "Данил", "Ильдар", "Мария", "Игорь", "Юлия"))