my_age = int(input("Enter your age: "))
friend_age = int(input("Enter your friend age: "))
sleep_days = int(input("Enter your sleep days per year: "))

who_oldest = str()
age_difference = abs(my_age - friend_age)

if my_age > friend_age:
    who_oldest = str("Ты старше")
else:
    who_oldest = str("Твой друг старше")



print(who_oldest)
print(f"Ваша разнциа в возрасте составляет: {age_difference} (год(а)/лет)")
print(f"За этот год ты поспал: {sleep_days*365} часов")
print(f"Оба ли старше 18 лет? {'Да' if my_age >= 18 and friend_age >= 18 else 'Нет'}")