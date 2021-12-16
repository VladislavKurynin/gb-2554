#Споздать список цен на товары до 20 шт
#Вывести на экран правильное отоброжение цен
#Вывести цены отсортированные по возрастанию, и в обратном порядке
Prices = [22.07, 56, 76.87, 44, 32, 1.05, 61, 21.54, 45.51, 29.99,
          88.06, 33.74, 71.24, 48, 60.45, 30.88, 14.81, 90.12, 84, 13, 67.01]

for i in Prices:
    rubl, cop = str(f"{i:.2f}").split(".")

    print(f"{rubl} руб {cop} коп,", end=" ")
print(f"ID base: {id(Prices)} - {Prices}")
Prices.sort()
print(f"ID change: {id(Prices)} - {Prices}")
n_list = sorted(Prices, reverse=True)
print(f"ID change: {id(n_list)} - {n_list}\n{n_list[:5][::-1]}")