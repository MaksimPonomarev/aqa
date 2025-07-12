# my_age = int(input("Enter your age: "))
# friend_age = int(input("Enter your friend age: "))
# sleep_hours = int(input("Enter your sleep hours per day: "))
#
# if my_age < 0 or friend_age < 0 or sleep_hours < 0:
#     print("Данные не могут быть отрицательными")
#     exit()
#
# who_oldest = str()
# age_difference = abs(my_age - friend_age)
#
# if my_age > friend_age:
#     who_oldest = str("Ты старше")
# else:
#     who_oldest = str("Твой друг старше")
#
#
#
# print(who_oldest)
# print(f"Ваша разнциа в возрасте составляет: {age_difference} (год(а)/лет)")
# print(f"За этот год ты поспал: {sleep_hours*365} часов")
# print(f"Оба ли старше 18 лет? {'Да' if my_age >= 18 and friend_age >= 18 else 'Нет'}")


while True:
    grade_1 = int(input("Enter your grade 1: "))
    grade_2 = int(input("Enter your grade 2: "))
    grade_3 = int(input("Enter your grade 3: "))

    num_list = [1,2,3,4,5]

    if grade_1 in num_list and grade_2 in num_list and grade_3 in num_list:
        break
    else:
        print("Цифры только от 1 до 5")


average = (grade_1 + grade_2 + grade_3) / 3
print(f"Среднее арифмитическое: {round(average, 2)}")