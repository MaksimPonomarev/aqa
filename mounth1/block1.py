
# name = 'Максим'
# age = 20
# sleep_hours = 8.2
# activity = True

#print(f"Имя: {name}\nВозраст: {age}\nСпит в среднем: {sleep_hours}\nАктивен: {activity}")



name = input("Enter your name: ")
age = int(input("Enter your age: "))
sleep_hours = float(input("Enter your sleep hours: "))
activity = input("Enter your activity (True/False): ").strip().lower() == "true"

print(f"Имя: {name}\nВозраст: {age}\nСпит в среднем: {sleep_hours}\nАктивен:{'Да' if activity else 'Нет'}")




