# def recursia(avlue):
#     print(avlue)
#     if avlue < 10:
#         recursia(avlue+1)
#     print(avlue)

# recursia(1)


# lambda - функция(анонимная,можно не присваивать ссылку на обьект, не имеет место в памяти,
# подходит для легких математических задач)
# def f(x):
#     return x **2
# print(f(3))
# aaa = lambda x: x**2
# print(aaa(3))


# aaa = lambda a,b,c: a+b+c
# print(aaa(2,3,4))

# def fun_decorator(func):  #параметр Func ссылка на некую функцию
#     def wrapper():
#         print("яячто то делаю до вызова")
        
#         print("яя что то делаю после вызова ")
#         func()
#     return wrapper


# def some_func():
#     print("вызов функции")

# f =fun_decorator(some_func)
# f()

#1
# a = lambda x, y, z: x * y * z

# print("Объём бассейна ", a(1,2,3))

#2
# a = lambda x: 365 - x
# print(a(2))

#3
# def recursia(x):
#     print(x)
#     if not x % 2 == 0:
        
#         recursia(x+2)
#         return x
# recursia(1)

#dop
# def num(n):
#     print(n)
#     if n == 100:
#         return n
#     else:
#         num(n+2)
# num(1)

#4
# def lset(a):
#     if a == set():
#         return a
#     else:
#         print(a.pop())
#         return lset(a)
# print(lset(a={'admin', 'admin2', 'admin3'}))

###########
#def fun_decorator(func):  #параметр Func ссылка на некую функцию
#     def wrapper():
#         print("яячто то делаю до вызова")
        
#         print("яя что то делаю после вызова ")
#         func()
#     return wrapper


# def some_func():
#     print("вызов функции")

# f =fun_decorator(some_func)
# f()
#1
# import random
# def a(x):
#     def wrapper():
        
#         b = []
#         for i in range(101):
#             b.append(i)
#         print(b)
#         def wrapper():
#             c = random.randint(10,50)
#             for i in c:
#                 if i in b:
#                     b.remove(i)
#                     print(b)
def a():
    lst = []
        