# # mats = ["blyat", "syka", "naxuy"]
# #
# # for i in range(len(mats)):
# #     print(f"Индекс в списке: {i}, Маты: {mats[i]}")
# #
# # for index, mats in enumerate(mats):
# #     print(f"{index}. {mats}")
# #
# # squares = [x for x in range(90)]
# # print(squares)
#
#
list_mov = []
count = 0
max_len_raw = 0
max_word = []
num = 0

while True:
    moves = input("Введи любимый фильм: ")
    list_mov.append(moves)
    count = count + 1
    if count == 5:
        break
    else:
        print(f"Фильм {count} из 5")

# for move in range(len(list_mov)):
#      print(f"{move + 1}. {list_mov[move]}")

for index, move in enumerate(reversed(list_mov)):
    print(f"{index + 1}. {move}")
    if len(move) > max_len_raw:
        max_len_raw = len(move)
        max_word.clear()
        max_word.append(f"{index + 1}. {move}")

print("Самое длинное слово:", *max_word)


for i in list_mov:
    num = len(i) + num

avg = num / len(list_mov)
print(f"Средняя длина названия: {round(avg, 2)}")

answer = input("Хочешь найти какой то фильм, который ты присал? ").lower()
if answer == "да":
    film = input("какой фильм хочешь найти? ")
    for index, mov in enumerate(list_mov):
        if mov.lower() == film.lower():
            print(f"Вот твой фильм: {film}, он под номером {index + 1}")



change_film = input("Хочешь поменять какой то фильм из списка? ").lower()
if change_film == "да":
    num_film = int(input("какой фильм хочешь менять? Укажи номер "))
    for index, mov in enumerate(list_mov):
        if index == num_film:
            print("зашел во вложенный цикл")
            list_mov.pop(num_film)
            add_film = input("Какой фильм хочешь поставить на это место?")
            list_mov.insert(num_film - 1, add_film)
print(f"Обновленный список фильмов: {list_mov}")