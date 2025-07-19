from functools import reduce

# def hello():
#     print("Хеллоу мир манера крутит мир")
# print(hello())
#
# def square(x):
#     return x**2
#
# print(square(8))
#
# def greet(name, role="qa engineer"):
#     print(f"Привет, {name}! Ты - {role}")
#
# greet("Максим")
# greet("Максим", "qa")

# def power(x, p=2):
#     return x**p
#
# print(power(5,10))
# print(power(5))

# def list_status(nums):
#     """множественный return, кортеж, len, sum"""
#     tuple(nums)
#     return nums
# list_a = [1,2,3,4,5,5,4,3,1,231,3,1,3,13,42,3,431,32,1,1,11,11,1]
# print(list_status(list_a))

#
# def flex_sum(*args, **kwargs):
#     sum_args = sum(args)
#     sum_kwargs = 0
#     for keys in kwargs:
#         value = kwargs.get(keys)
#         if isinstance(value,(int,float)):
#             sum_kwargs = sum_kwargs + value
#         else:
#             return "Ты зачем сюда строку пихнул? ТОЛЬКО ЦИФРЫ"
#
#     return sum_args + sum_kwargs
#
# print(flex_sum(22,92, a=9,b=456,c=5,d="hfyhv"))



# def apply(func, *iterable):
#     new_list = []
#     for i in iterable:
#         new_list.append(func(i))
#     return new_list
#
# print(apply(lambda x: x**2, 3,4,5,6,7))


# def sort_by_lenght(words, reverse=False):
#     return sorted(words, key=lambda x: len(x), reverse=reverse)
#
#
# a = ['efwfewf','12erfwsvc','1232222222222222222222222222222222222222222dfs','1','12','123']
# print(sort_by_lenght(a))
#
#




def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


a = make_counter()
for i in range(5):
    print(a())
#
# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         list_num = []
#         for i in range(n):
#             list_num.append(i+1)
#         return reduce((lambda x,y: x*y), list_num)


# print(factorial(5))
#
# def factorial_v_2(n):
#     if n <= 1:
#         return 1
#     return n * factorial_v_2(n-1)
#
# print(factorial_v_2(5))
#
# def fibo(n, a=0,b=1):
#     while True:
#         c = a + b
#         yield a+b
#         a = b
#         b = c
#         n -= 1
#         if n == 0:
#             break
#
# n = int(input("До какого чилса? "))
# for i in fibo(n):
#     print(i)





# def iii():
#     i = 0
#     while True:
#         yield i * 2
#         i += 1
#
#
#
# count = 0
# for i in iii():
#     if count >= 15:
#         break
#     print(i)
#     count += 1
#
