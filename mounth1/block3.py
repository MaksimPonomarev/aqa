while True:
    weight = float(input("Введите ваш вес в килограммах: "))
    height = float(input("Введите ваш рост в сантиметрах: "))/100
    if weight > 0 and height > 0:
        break
    else:
        print("Только положитльные значения")

bmi = weight / (height ** 2)

print(f"Ваш ИМТ: {round(bmi, 2)}")

if bmi < 18.5:
    print("Недовес")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Нормальный вес")
elif bmi >= 25 and bmi <= 29.9:
    print("Избыточный вес")
else:
    print("Ожирение")