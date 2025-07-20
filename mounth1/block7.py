# class Example:
#     def __init__(self):
#         self.public = "доступно всем"
#         self._protected = "доступно, но не трогай"
#         self.__private = "спрятано"
#
# obj = Example()
# print(obj.public)       # работает
# print(obj._protected)   # работает, но не рекомендуется
# print(obj.__private)    # ошибка: нет такого поля!

#
# class User:
#     def __init__(self, name, password):
#         self.name = name
#         self.__password = password
#
#     def get_info(self):
#         return f"Имя {self.name}"
#
# u = User("Али", "1234")
# print(u.get_info())
# print(u.name)
# print(dir(u))
# print(u._User__password)

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
#
#
#     def get_balance(self):
#         return self.__balance
#
#     def set_balance(self, amount):
#         if amount < 0:
#             raise ValueError("Баланс не может быть отрицательным")
#         self.__balance = amount
#
# a = BankAccount("Maksim", 100)
# print(a.get_balance())
# a.set_balance(500)
# print(a.get_balance())

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError
#         self.__price = value
#
#
# p = Product("Монитор", 15000)
# print(p.price)         # → 15000
#
# p.price = 20000        # ✅
# print(p.price)         # → 20000
#
# p.price = -500         # ❌ ValueError

# class Person:
#
#     def validate_age(self, value):
#         if value < 0 or value > 150:
#             raise ValueError("Возраст от 0 до 150")
#
#     def __init__(self, name, age):
#         self.validate_age(age)
#         self.name = name
#         self.__age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         self.validate_age(value)
#         self.__age = value
# #
# p = Person("Maksim", 20)
# print(p.age)
# a = Person("Masha", 30)
# a.age = 32
# print(a.age)
# c = Person("Jora", 5)
#
# for i in range(5):
#     years = int(input("Введи цифру: "))
#     try:
#         c.age = years
#     except ValueError as e:
#         print(f"Ошибка при изменении возраста {e}")

class Product:

    def validation_price(self, price):
        if price < 0:
            raise ValueError("Только положительные числа")

    def validation_discount(self, discount):
        if discount < 0 or discount > 100:
            raise ValueError("Только положительные числа")

    def __init__(self, name, price, discount):
        self.name = name
        self.__price = price
        self.__discount = discount

    @property
    def final_price(self):
        self.validation_price(self.__price)
        self.validation_discount(self.__discount)
        return self.__price * (1-self.__discount/100)

    @property
    def discount(self):
        self.validation_discount(self.__discount)
        return self.__discount

    @discount.setter
    def discount(self, value):
        self.validation_discount(value)
        self.__discount = value
        return self.__discount

    @property
    def price(self):
        self.validation_price(self.__price)
        return self.__price

    @price.setter
    def price(self, value):
        self.validation_price(value)
        self.__price = value
        return self.__price


p = Product("Кофеварка", 10000, 20)

try:

    print(p.final_price)  # → 10000 (без скидки)

    p.discount = 20
    print(p.final_price)  # → 8000.0

    p.price = 12000
    print(p.final_price)  # → 9600.0

    p.discount = 150

except ValueError as e:
    print("Пупупу")
