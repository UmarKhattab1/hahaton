# return
# def hello():
#     return "Agil where are you my love baby"
# # message = hello()
# print(hello())

# def sum(a,b):
#     return a +b
    
# print(sum(2,5))
# def square(x):
#     return x ** 2
# print(square(3))

# def get_max(a,b):
#     return a if a > b else b
# print(get_max(6,6))
# from math import *

# def cylinder():
#     r = float(input(":    "))
#     h = float(input(":    "))
#     side = 2 * pi * r * h
#     circle = pi * r**2
#     full = side + 2 * circle
#     return side,circle,full
# print(cylinder())

# def cylinder(r,h):
    
#     side = 2 * pi * r * h
#     circle = pi * r**2
#     full = side + 2 * circle
#     return side,circle,full
# print(cylinder(2.34,123.123))


# *args and **kwargs


# def name(*args):
#     for i in args:
#         return i
# word =("kak dela s funkciyami?")

# print(name(word))


# def find_animal(*args):
#     if "dog" in args:
#         return True
# print(find_animal("cat","mouse",12,32,False,"dog"))

# def infor(game, **kwargs):
#     players = []
#     numbers = []
#     if game =="football":
#         for k,w in kwargs.items():
#             players.append(k)
#             numbers.append(w)
#         return game,players,numbers
# print(infor(game = "football",alex = "first", bob = "second",messi = "ten",ronaldo = "seven"))

# def phone_book(**kwargs):
#     name = []
#     phone = []
#     for k,v in kwargs.items():
#         name.append(k)
#         phone.append(v)
#     return name,phone
# print(phone_book(agil = "+9969379992", egida = "+996love"))
# from random import choice
# def gen_number():
#     i = 0
#     print('0444', end='')
#     while i <= 5:
#         n2 = [1,4,5,7,9,0]
#         print(choice(n2), end='') 
#         i = i + 1
# gen_number()

#1
# def value():
#     def add(x, y):
#         return x + y
#     print(add(13, 12))
#     def substract(x, y):
#         return x - y
#     print(12, 15)
#     def multiply(x, y):
#         return x * y1
#     print(mul)

#4
# def order(x, y):
#     # x = input('what do you wonna eat: ')
#     # y = input('what do ypu wonna drink: ')
#     a = open('menu.txt', mode='a', encoding='utf-8')
#     a.write(x, y)
#     return open('menu.txt', mode='r', encoding='utf-8')
# print(order())


#2
# def count(a):
    
#     b = 0
#     for i in a:

#         b+=1


#     print(b)

# count('asdfgkjhgf')


#3
# def tpl():
#     a = {'umar':2, 'bejs':3, 'kesha' : 5}
#     b = {'bakr' : 6, 'beka': 123}
#     a.update(b)
#     print(a)
# tpl()

# dop 3
# def dict(a, b):
#     a.update(b)
#     return a
# a = {input('a; '), input('b: ')}
# b = {input('a:' ), input('b; ')}
# print(dict(a,b)) 

#4
# food = input('what do you wonna eat: ')
# drink = input('what do you wonna drink; ')
# def enter():
#     a = open('menu.txt', mode = 'w', encoding='utf-8')
#     a.write(f'{food}, {drink}')
#     # a.write(drink)
#     a.close()
#     print(a)
# enter()

#5
# def name():
#     a = input("enter the name of file: ")
#     b = open(a, mode='w', encoding="utf-8")
#     b.write('hi')
#     b.close()
#     return open(a, mode="r", encoding="utf-8")
# print(name())

#1
# def func1():
#     print('func1')
#     def func2():
#         print('func2')
#     func2()
# func1()

#2
# def dict():
#     a = {'umar': 1, 'baeka':2, 'bakr':3}
#     b = tuple(a.keys())
#     print(b)
#     c = tuple(a.values())
#     print(c)
# dict()

 #dop   
# def dict(*args):
#     for i in args:
#         a = tuple(i.keys())
#         b = tuple(i.values())
#         print(a, b)
# dict({'umar': 1, 'baeka':2, 'bakr':3})    

#3
# def count():
#     n = int(input())
#     i = 2
#     while i < n:
#         if n % i == 0:
#             a = False
#         i += 1
#     if a:
#         print('ok')
#     else:
#         print('no')
# count()

#1
# def lst(a, b):
#     c = []
#     c.append(a)
#     c.append(b)
#     print(c)
# lst(3, 'umar')

#2
# def count():
 
#     a = int(input())
#     b = 1
#     while b < a+1:
#         print(b)
#         b += 1
# count()
#3
# def zarplata(a, b=5000):

#     print(a, b)
# zarplata('umar', 300000000)
# zarplata('umar')

#4
# def count(a):
#     i = 0 
#     c = []
#     while i < a:
#         c.append(i)
#         print(c)
#         i += 1
        
# count(8) 

