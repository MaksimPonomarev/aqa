# a = []
# a.append("str1")
# a.append("str2")
# a.append("str3")
# a.append(["str4"])
# print(a)
#
# a = [1,2,3]
# a.append([4,5])
# a.extend([4,5])
# print(a)
#
# a = ["а", "б", "в", "г", "д"]
# print(a[1:4])
# print(a[-1])
# a.insert(2,"new")
# print(a)
#
# a = [1,2,3,2,4]
# a.remove(2)
# print(a)
# a.pop(2)
# print(a)
# a.clear()
# print(a)

#
# a = [1,2,3]
# print(a)
# b = a
# print(b)
# c = a.copy()
# print(c)
# b[0] = "new"
# print(b)
# c[0] = "new"
# print(c)
# print(a)

# matrix = [[1,2], [3,4]]
# matrix[1][1] = 999
# matrix.append([5,6])
# matrix.extend([5,6])
# print(matrix)
# count = 0
# for i in matrix:
#     if isinstance(i, list):
#         count +=1
#     else:
#         print("Не список")
# print(count)

# print(matrix)
#
# a = [5,2,9,1]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
#
# a = ["кот", "пёс", "кот", "птица"]
# print(a.count("кот"))
# print(a.index("кот"))
# try:
#     print(a.index("мышь"))
# except ValueError as e:
#     print(e)

#
# a = [1,4,7,10,3]
# total = 0
# for i in a:
#     total += i
# print(total)
#
# a = ["кот", "пёс", "мышь"]
# for index, elem in enumerate(a):
#     print(f"Элемент {index}: {elem}")
#
# a = [4, -2, 0, 5, -1]
# for i in a:
#     if i >= 0:
#         print(i)


# a = [30,2,7,3,1,9]
# max = a[0]
# for i in a:
#     if max < i:
#         max = i
# print(max)

# a = [1, 2, 3, 4, 5, 6]
# count = 0
# for i in a:
#     if i % 2 == 0:
#         count += 1
#
# print(count)


# a = [[1, 2], [3, 4], [5]]
# count = 0
# for row in a:
#     for elem in row:
#         count += elem
# print(count)

#
# a = ["a","b","c"]
# b = []
# for i in a:
#     b.append(i.upper())
# print(b)
#
# a = [1, -2, 3, -4, 5]
# b = []
# for i in a:
#     if i >= 0:
#         b.append(i)
# print(b)


# matrix = [[1, 2], [3, 4]]
# flattened = [x for row in matrix for x in row]
# print(flattened)




#Задачи на списковые включения (List Comprehension)
# a = [1,2,3,4]
# b = [x*2 for x in a]
# print(b)
#
# a = ["python", "java", "c++"]
# b = [x.upper() for x in a]
# print(b)
#
#
# a = [-4, 3, -2, 0, 1]
# b = [x for x in a if x>0]
# print(b)
#
# a = [1, 2, 3, 4, 5]
# b = [x**2 for x in a if x%2==0]
# print(b)
#
# a = [1, 2, 3, 4, 5]
# b = ["чет" if x%2==0 else "нечет" for x in a ]
# print(b)
#
# a = [[1, 2], [3, 4], [5, 6]]
# b = [x for row in a for x in row]
# print(b)
#
# a = (1,2,3,4)
# print(len(a))
# print(a[1])
#
# tup = (10,20,30)
# a,b,c = tup
# print(a,b,c)
#
# a = (1,2,3)
# try:
#     a[0] = 99
# except TypeError as e:
#     print(e)
# print(a)
#
# a = (7,)
# print(type(a))
#
# a = (1,2,2,3,2)
# print(a.count(2))
# print(a.index(2))
#
# a = [("a", 1), ("b", 2), ("c", 3)]
# for letter, number in a:
#     print("Буква:", letter)
#     print("Число:", number)


# a = {
#     (0, 0): "начало",
#     (1, 2): "точка A"
# }
#
# text = a[(1,2)]
# print(text)
#
# for key in a.keys():
#     x,y=key
#     if x == 1 and y == 2:
#         print(a[key])


# data = ((1, 2), (3, 4), (5, 6))
# count=0
# for elem in data:
#     for i in elem:
#         count+=i
#
# print(count)



#Задачи на словари
# person = {
#     "name": "Maksim",
#     "age": 20,
#     "city": "Moscow"
# }
# print(person["city"])
#
# user = {
#     "login": "user123"
# }
#
# user["email"] = "test@example.com"
# user["login"] = "admin"
#
# data = {
#     "x": 1,
#     "y": 2
# }
# print(data.get("z", "Нет данных"))
#
# scores = {
#     "Анна": 90,
#     "Борис": 80,
#     "Вера": 95
# }
# for key, values in scores.items():
#     print(f"{key} получил(а) {values}")
#

# string_a = "hello"
# dict_with_string = {}
# for i in string_a:
#     if i in dict_with_string.keys():
#         dict_with_string[i] += 1
#     else:
#         dict_with_string[i] = 1
#
# print(dict_with_string)
#
# d = {"a": 1, "b": 2, "c": 3}
# del d["b"]
# print(d)
# d = {"a": 1, "b": 2, "c": 3}
# print(d.pop("b"))

# user = {
#     "name": "Али",
#     "profile": {
#         "age": 30,
#         "email": "ali@example.com"
#     }
# }
#
# print(user.get("name"))
# print(user["profile"]["email"])


# groups = {
#     "QA": ["Али", "Зара"],
#     "Dev": ["Магомед", "Омар"]
# }
# a = " ".join(groups["QA"])
# b = " ".join(groups["Dev"])
# print(f"QA: {a}")
# print(f"QA: {a} и Dev: {b}")
#
# users = [
#     {"id": 1, "name": "Али"},
#     {"id": 2, "name": "Зара"},
#     {"id": 3, "name": "Омар"}
# ]
#
# print(users[1]["name"])

#
# projects = {
#     "P1": {"status": "done"},
#     "P2": {"status": "in progress"},
#     "P3": {"status": "done"},
#     "P4": {"status": "in review"}
# }
# count = 0
#
# for key, value in projects.items():
#     for key1, value1 in value.items():
#         if value1.lower() == "done":
#             count += 1
#
# print(count)

#
# user = {
#     "name": "Али",
#     "skills": ["Python", "Selenium", "Git"]
# }
#
# user["skills"].append("Docker")
# res = ", ".join(user["skills"])
# print(res)


#множества
# a = [1, 2, 2, 3, 3, 3, 4]
# print(list(set(a)))
#
# s = {1, 3, 5, 7}
# if 5 in s:
#     print("Есть")
# else:
#     print("Нет")

# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# c = (set(a)).union(set(b))
# print(c)
# d = (set(a)).intersection(set(b))
# print(d)

# a = [1, 2, 3, 4, 5]
# b = [4, 5, 6]
# c = (set(a)).difference(set(b))
# print(c)

# a = {1, 2, 3}
# b = {3, 4, 5}
# c = (set(b)).symmetric_difference(set(a))
# print(c)

#frozenset
# a = frozenset([1,2,3])
# try:
#     a.add(4)
# except AttributeError as e:
#     print(e)

# a = frozenset([1, 2, 3])
# b = frozenset([3, 4, 5])
# c = a.intersection(b)
# print(c)
# d = a.symmetric_difference(b)
# print(d)
#а это нормально что тут такой вывод странный?

# c = {
#     frozenset([1, 2]): "двойка",
#     frozenset([3, 4]): "четвёрка"
# }
#
# print(c.get(frozenset([1,2])))


#комбинирование структур данных
# users = [
#     {"name": "Али", "skills": ["Python", "Git"]},
#     {"name": "Зара", "skills": ["Java", "Docker"]},
#     {"name": "Магомед", "skills": ["Python", "Docker"]}
# ]
# set_skills = set()
# for user in users:
#     for skill in user["skills"]:
#         set_skills.add(skill)
#         if skill.lower() == "python":
#             print(user.get("name"))
# res = ", ".join(set_skills)
#
# print(res)

#
# groups = {
#     "QA": ["Али", "Зара"],
#     "Dev": ["Магомед", "Омар", "Иса"]
# }
# count = 0
# for group, list_name in groups.items():
#     count += len(list_name)
#
# print(count)

# tests = [
#     {"id": 1, "title": "Login test", "passed": True},
#     {"id": 2, "title": "Logout test", "passed": False},
#     {"id": 3, "title": "Profile test", "passed": True}
# ]
#
# for test in tests:
#     if test["passed"] == False:
#         print(test["title"])


#
# projects = {
#     "P1": {"api", "auth"},
#     "P2": {"ui", "smoke"},
#     "P3": {"api", "smoke"}
# }
#
# for project, tags in projects.items():
#     if "api" in tags:
#         print(project)

# runs = [
#     {"test_id": 1, "status": "passed", "tags": {"smoke", "regression"}},
#     {"test_id": 2, "status": "failed", "tags": {"api"}},
#     {"test_id": 3, "status": "passed", "tags": {"ui", "smoke"}}
# ]
#
# for run in runs:
#     if run["status"] == "passed" and "smoke" in run["tags"]:
#         print(run["test_id"])