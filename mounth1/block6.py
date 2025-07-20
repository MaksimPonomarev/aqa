# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def __str__(self):
#         return f"Книга: {self.title}, автор: {self.author}"
#
#     def describe(self):
#         print(f"Книга: {self.title}, автор: {self.author}")
#
#
# a = Book("ert","eefef")
# b = Book("efgrgaf", "weferffdf")
# a.describe()
# b.describe()
# print(a)
#
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         print(f"Привет, меня зовут {self.name}, и мне {self.age} лет")
#
#     def is_adult(self):
#         return self.age >= 18
#
#
# user_1 = User("Максим", 20)
# user_1.introduce()
# print(user_1.is_adult())
#
#
# class Product:
#     def __init__(self, name, price):
#         self.name=name
#         self.price=price
#
#     def apply_discount(self, percent):
#         self.price=self.price - self.price*(percent/100)
#         print(type(self.price))
#         return self.price
#
# a = Product("хлеб", 100)
# print(a.apply_discount(20))



# class Parent:
#     def hello(self):
#         print("Привет от родителя!")
#
# class Child(Parent):
#     def hello(self):
#         print("Привет от потомка!")
#
#
# Child.mro()


# ЗАДАЧА 1,2. Расширение конструктора с помощью super()
# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
#
#     def get_info(self):
#         return f"Имя: {self.name}, эмаил: {self.email}"
#
# class Admin(User):
#     def __init__(self,name, email, access_level):
#         super().__init__(name, email)
#         self.access_level = access_level
#
#     def get_info(self):
#         info = super().get_info()
#         return f"{info}, Уровень доступа: {self.access_level}"
#
# a = Admin("Максим", "fewfw@adef.com", "high")
# b = User("Антон", "ауцмкца")
# print(a.get_info())
# print(b.get_info())


# class User:
#     def __init__(self, name, email):
#         self.name=name
#         self.email=email
#
#     def get_info(self):
#         return f"пользователь {self.name}, email: {self.email}"
#
# class Guest(User):
#     def __init__(self, name):
#         self.name=name
#     def get_info(self):
#         return f"Гость {self.name} (гостевой доступ)"
#
#
# a = Guest("Магомед")
# b = User("Славик", "fokrwowef")
# print(a.get_info())
# print(b.get_info())


# class User:
#     def __init__(self, name, email):
#         self.name=name
#         self.email=email
#
#     def get_info(self):
#         return f"Имя: {self.name}, email: {self.email}"
#
#
# class Moderator(User):
#     def __init__(self, name, email, can_ban_users):
#         super().__init__(name, email)
#         self.can_ban_users=bool(can_ban_users)
#
#     def get_info(self):
#         info = super().get_info()
#         return f"{info}, Может банить пользователей" if self.can_ban_users == True else f"{info}. Не может банить пользователей"
#
#
# a = User("Максим", "fwef@efwf.com")
# b = Moderator("Человек", "уацуауац", True)
# c = Moderator("fwewef","wefwef",False)
# print(a.get_info())
# print(b.get_info())
# print(c.get_info())
#
# class User():
#     def __init__(self, name):
#         self.name=name
#
#     def greet(self):
#         return f"Привет, {self.name}"
#
# class Guest(User):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def greet(self):
#         return f"Привет, {self.name}. У вас ограниченные права доступа."
#
# class Admin(User):
#     def __init__(self,name):
#         super().__init__(name)
#
#     def greet(self):
#         info = super().greet()
#         return f"{info}, \nДобро пожаловать в админ-панель"
#
#
# u = User("Али")
# g = Guest("Мурад")
# a = Admin("Фатима")
#
# print(u.greet())
# print(g.greet())
# print(a.greet())
#
#
# class A:
#     def greet(self):
#         print("Имя класса А")
#
# class B(A):
#     def greet(self):
#
#         print("Имя класса B")
#         super().greet()
#
# class C(A):
#     def greet(self):
#
#         print("Имя класса C")
#         super().greet()
#
# class D(B,C):
#     def greet(self):
#
#         print("Имя класса D")
#         super().greet()
#
# d = D()
# d.greet()
# print(D.__mro__)

#
# class User():
#     def save(self):
#         print("Сохраняем данные пользователя")
#
# class LoggerMixin(User):
#     def save(self):
#         print("Лог: Данные сохранены")
#         super().save()
#
# class Admin(LoggerMixin, User):
#     def save(self):
#         print("Сохраняем админские настройки")
#         super().save()
#
# a = Admin()
# a.save()



# class User():
#     def save(self):
#         print("Сохраняем данные пользователя")
#
# class NotifierMixin():
#     def save(self):
#         print("Уведомление: пользователь обновлен")
#         super().save()
#
# class LoggerMixin():
#     def save(self):
#         print("Лог: пользователь сохранен")
#         super().save()
#
# class Admin(NotifierMixin, LoggerMixin, User):
#     def save(self):
#         print("Сохраняем админские настройки")
#         super().save()
#
# a=Admin()
# a.save()
