# a =[-1,-2,-3]
# print(all(a)) # показывает все ли обьекты True
# print(any(a)) # показывает есть ли хотя-бы один обьект True

# num=[1,2,3,4,6,7]
# print(min(num),max(num)) #  мин или макс число в списке

# print(abs(-66)) № показывает масимум этого числа -66 то будет 66

# x=1
# print(eval("x!=1")) работает как int/str в зависимоти от задачи
# print(eval("x*2"))

# a = 123123.1231231
# c = 123123.123123
# print(round(c,4)) округление после точки до заданного числа


# salary = [123123,123123,34,6] переворачивает список
# print(list(reversed(salary)))
# try:
#     a = int(input("number1:   "))
#     b = int(input("number 2 :   "))
#     print(a+b)
# except:

#     print("нужно ввести только числа, понятно?")

# finally:
#     print("конец")

#1
# values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
# b = []
# try:
#     for i in values:
#         if set(i):
#             b.append(True)
#         else:
#             b.append(False)
        
#     if all(b) == True:
#         print("ok")
#     else:
#         print("no")
# except:
#     print("error")

#2
# num1 = int(input("num1: "))
# num2 = int(input("num2: "))
# num3 = int(input("num3: "))
# num4 = int(input("num4: "))
# num5 = int(input("num5: "))
# a = num1, num2, num3, num4, num5
# b = set()
# try:
#     for i in a:
#         b.add(i)
#         print(min(b)) 
        
# except:
#     print("only numbers")   

#2
# try:
#     b = set()
#     i = 0
#     while i < 5+1:
#         a = int(input("enter the number: "))
#         i +=1
#         b.add(a)
#     print(min(b))
# except ValueError:
#     print("str")

#3
# a = "all", "any", "abs", "min", "eval", "reversed", "max", "slice", "round"
# i = input('enter the func: ')
# try:
#     for i in a:
#         if i in a:
#             print(i)
#             break
#         else:
#             print('this is not func un python')
# except:
#     print('no')
    
#4
