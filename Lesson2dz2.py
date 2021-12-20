#В данном списке нужно обособить каждое целое число кавычками
#Дополнить нулем до двух целочисленных разрядов
#Сформировать из обратного в строку
error_list = ['В', '5', 'часов', '17', 'минут', 'темпиратура', 'воздуха', 'была', '+5', 'градусов']
nice_list = []

for i in error_list:
    if i.replace("+" ,"").replace("-", "").isdigit():
        if i.isdigit():
            nice_list.append(f"'{int(i):02}'")
        else:
            nice_list.append(f"'{i[0]}{int(i[1:]):02}'")
    else:
        nice_list.append(i)
print(nice_list)
print(" ".join(nice_list))
