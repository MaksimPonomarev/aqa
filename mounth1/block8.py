from datetime import datetime

# try:
#     a = int(input("Числоа а: "))
#     b = int(input("Число b: "))
#     c = a/b
# except ValueError:
#     print("Это не число")
# except ZeroDivisionError:
#     print("На 0 делить нельзя")
# else:
#     print("результат деления:", c)
# finally:
#     print("Завершено")

# def safe_divide(a,b):
#     try:
#         if b == 0:
#             raise ZeroDivisionError("На 0 делить нелья")
#         c = a/b
#     except TypeError:
#         print("Это не число")
#     else:
#         return c
#     finally:
#         print("Завершено")
#
#
# print(safe_divide(10, 0))     # Ошибка: на ноль делить нельзя
# print(safe_divide("10", 5))   # Ошибка: введено не число
# print(safe_divide(10, 2))     # 5.0




#
# | Режим  | Назначение                       |
# | ------ | -------------------------------- |
# | `"r"`  | чтение (файл должен быть)        |
# | `"w"`  | запись (удаляет старое)          |
# | `"a"`  | добавление в конец               |
# | `"x"`  | создание (ошибка, если уже есть) |
# | `"rb"` | чтение в бинарном режиме         |
# | `"r+"` | чтение и запись                  |








file_1 = "C:/Users/mr/Desktop/test1.txt"
file_2 = "C:/Users/mr/Desktop/test2.txt"
file_3 = "C:/Users/mr/Desktop/test3.txt"

# def read_file(file):
#     try:
#         with open(file, "r", encoding="utf-8") as f:
#             lines = f.readlines()
#             for i, line in enumerate(lines, start=1):
#                 print(f"{i}. {line.strip()}")
#
#     except FileNotFoundError:
#         print("Файл не найден, проверьте путь к файлу")
#     except PermissionError:
#         print("Нет прав на чтение файла.")
#
#
# read_file(file_a)

# def log_message(file_path, message):
#     try:
#         with open(file_path, "a", encoding="utf-8") as f:
#             now = datetime.now()
#             formatted = now.strftime("%d-%m-%Y %H:%M:%S")
#             f.write(f"{formatted}: {message}\n")
#     except FileNotFoundError:
#         print("Файл не найден, проверьте путь к файлу")
#     except PermissionError:
#         print("Нет прав на чтение файла.")
#
#
# def read_file(file_path):
#     try:
#         with open (file_path, "r", encoding="utf-8") as f:
#             return f.read()
#
#     except FileNotFoundError:
#         print("Файл не найден, проверьте путь к файлу")
#     except PermissionError:
#         print("Нет прав на чтение файла.")
#
#
# log_message(file_a, "addddd")
# print(read_file(file_a))
#
# def work_with_file(file_patch):
#     all_num_line_with_space = 0
#     all_num_line_without_space = 0
#     try:
#         with open(file_patch,"r", encoding="utf-8") as f:
#             text = f.read()
#             lines = text.splitlines()
#             print(f"Количество строк: {len(lines)}")
#             for line in lines:
#                 all_num_line_without_space += len(line.replace(" ", ""))
#                 all_num_line_with_space += len(line)
#             print(f"Количество символов всего в тексте без пробелов: {all_num_line_without_space}")
#             print(f"Количество символов всего в тексте c пробелами: {all_num_line_with_space}")
#
#     except FileNotFoundError:
#         print("Файл не найден, проверьте путь к файлу")
#     except PermissionError:
#         print("Нет прав на чтение файла.")
#
# work_with_file(file_a)
#
# def save_lines_to_file(file_patch, lines):
#     try:
#         with open(file_patch, "w", encoding="utf-8") as f:
#             for line in lines:
#                 f.write(f"{line}\n")
#     except FileNotFoundError:
#         print("Файл не найден, проверьте путь к файлу")
#     except PermissionError:
#         print("Нет прав на чтение файла.")
#
#
# def read_file(file_patch):
#     try:
#         with open(file_patch, "r", encoding="utf-8") as f:
#             return f.read()
#     except FileNotFoundError:
#         print("Файл не найден, проверьте путь к файлу")
#     except PermissionError:
#         print("Нет прав на чтение файла.")
#
#
# lines_a = ["Первая строка", "Вторая строка", "Третья строка"]
# save_lines_to_file(file_a, lines_a)
#
# print(read_file(file_a))
#
# def search_lines_by_keyword(file_patch, keyword):
#     try:
#         with open(file_patch, "r", encoding="utf-8") as f:
#             text = f.read()
#             line = text.splitlines()
#             for i, word in enumerate (line, start=1):
#                 if keyword.lower() in word.lower():
#                     print(f"Слово найдено: в строке №{i}, {word}")
#
#     except FileNotFoundError:
#         print("Файл не найден, проверьте путь к файлу")
#     except PermissionError:
#         print("Нет прав на чтение файла.")
#
# search_lines_by_keyword(file_a, "Первая")

# def analyze_text_status(file_patch):
#     try:
#         with open(file_patch, "r", encoding="utf-8") as f:
#             text = f.read()
#             line = text.splitlines()
#             total_chars = 0
#             chars_with_space = 0
#             list_words = []
#             dict = {}
#             for row in line:
#                 total_chars += len(row)
#                 chars_with_space += len(row.replace(" ", ""))
#                 clear_text = row.replace("."," ").replace(","," ")
#                 peremennaya = clear_text.lower().split()
#                 list_words += peremennaya
#                 for char in row:
#                     if char.isalpha():
#                         char = char.lower()
#                         if char in dict:
#                             dict[char] += 1
#                         else:
#                             dict[char] = 1
#
#
#
#
#
#             print(f"Общее количество символов: {total_chars}")
#             print(f"Общее количество символов без пробелов {chars_with_space}")
#             print(f"Количество слов: {len(list_words)}")
#             print(f"Количество каждой буквы: {dict}")
#
#     except FileNotFoundError:
#         print("Файл не найден, проверьте путь к файлу")
#     except PermissionError:
#         print("Нет прав на чтение файла.")
#
# analyze_text_status(file_a)


# def merge_files(file1_path, file2_path, output_path):
#     try:
#         with open(file1_path, "r", encoding="utf-8") as f1, \
#              open(file2_path, "r", encoding="utf-8") as f2, \
#              open(output_path, "w", encoding="utf-8") as f3:
#
#             f3.writelines(f1.readlines())
#             f3.writelines(f2.readlines())
#
#
#     except FileNotFoundError:
#         print("Файл не найден, проверьте путь к файлу")
#     except PermissionError:
#         print("Нет прав на чтение файла.")
#
# merge_files(file_1, file_2, file_3)


# def file_comparison(file1_path, file2_path):
#     count = 0
#     last_str = []
#     num_of_mis_lines = 0
#     num_of_non_match_lines = {}
#     try:
#         with open(file1_path, "r", encoding="utf-8") as f1, \
#              open(file2_path, "r", encoding="utf-8") as f2:
#
#
#             while True:
#                 text1 = f1.readline().lower().strip("., !@#$%^&*()_+").splitlines()
#                 text2 = f2.readline().lower().strip("., !@#$%^&*()_+").splitlines()
#                 count += 1
#
#                 #остаток строк
#                 if text1 == [] and text2 == []:
#                     break
#                 elif text1 == []:
#                     last_str.append(text2)
#                     per_file = 1
#
#                 elif text2 == []:
#                     last_str.append(text1)
#                     per_file = 2
#
#                 #сравнние строк
#                 elif text1 != text2:
#                     num_of_mis_lines += 1
#                     num_of_non_match_lines[count] = (text1, text2)
#
#
#             #вывод значений в принт без скобок
#             str_keys_a = ", ".join(str(key) for key in list(num_of_non_match_lines.keys()))
#             result = []
#             for elem in last_str:
#                 result_str = elem[0]
#                 result.append(result_str)
#
#             result_a = ", | ".join(result)
#
#
#
#             print(f"Количество не совпадающих строк: {num_of_mis_lines}")
#             print(f"Номера строк, в которых содержимое отличается: {str_keys_a}")
#             for val in list(num_of_non_match_lines.values()):
#                 first_str = ", ".join(val[0])
#                 second_str = ", ".join(val[1])
#                 print(f"Строка из файла 1: {first_str} | Cтрока из файла 2: {second_str}")
#             print(f"Остаток строк от файл №{per_file}: {result_a}")
#
#
#
#     except FileNotFoundError:
#         print("Файл не найден, проверьте путь к файлу")
#     except PermissionError:
#         print("Нет прав на чтение файла.")
#
# file_comparison(file_1, file_2)



