while True:
    weight = float(input("Введите ваш вес в килограммах: "))
    height = float(input("Введите ваш рост в сантиметрах: "))/100
    if weight > 0 and height > 0:
        break
    else:
        print("Только положитльные значения")

bmi = weight / (height ** 2)

print(f"Ваш ИМТ: {bmi}")

if bmi < 18.5:
    print("Недовес")
if bmi >= 18.5 and bmi <= 24.9:
    print("Нормальный вес")
if bmi >= 25 and bmi <= 29.9:
    print("Избыточный вес")
if bmi > 30:
    print("Ожирение")