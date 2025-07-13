# mats = ["blyat", "syka", "naxuy"]
#
# for i in range(len(mats)):
#     print(f"Индекс в списке: {i}, Маты: {mats[i]}")
#
# for index, mats in enumerate(mats):
#     print(f"{index}. {mats}")
#
# squares = [x for x in range(90)]
# print(squares)


list_mov = []
count = 0
max_len_raw = 0
max_word = []

while True:
    moves = input("Введи любимый фильм: ")
    list_mov.append(moves)
    count = count + 1
    if count == 3:
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