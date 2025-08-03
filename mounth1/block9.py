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

a = [1, -2, 3, -4, 5]
b = []
for i in a:
    if i >= 0:
        b.append(i)
print(b)