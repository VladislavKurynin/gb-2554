#Дан список, с ошибками
#Вывести на экран правильный список

Error_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in Error_list:
    print(f"Привет, {i.split()[-1].title()}!")

