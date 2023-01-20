# a = []
# i = 0
# while i < 5:
#     b = int(input("enter the number: "))
# letters = 'ФЫОроииоРФИИРлорчот'

# a = []
# b = []
# for i in letters:
#     if  i == i.upper():
#         a.append(i)
#     else:
#         b.append(i)

# print(a)
# print(b)
    

# secret_names = ['Мавпродош', 'Лорнектиф', 'Древерол', 'Фиригарпиг', 'Клодобродыч']
# name = input('enter the name: ')
# other_names = []
# for i in secret_names:

#     if i == name:
#         print(f"Ты – свой. Приветствую, любезный {name}")
#         exit()
        
#     else:
#         other_names.append(name)
#         print(other_names)
#         break

# a = int(input("enter the number: "))
# b = int(input("enter the number: "))


#kalkulator
# try:
#     while True:
#         num1 = int(input('enter thr number: '))
#         num2 = int(input('enter the number: '))
#         symvol = input("enter the symvol: +, -, *, /: ")
#         if symvol == '+':
#             print(num1 + num2) 
#         elif symvol == '-':
#             print(num1 - num2)
#         elif symvol == '*':
#             print(num1 * num2)
#         elif symvol == '/':
#             print(num1 / num2)
           
#         quastion = input("do you wonna go on: yes, no: ")
#         if quastion == "yes":
#                 continue
#         else:
#                 break
# except ZeroDivisionError:
#     print('number cannot be divided by zero!')
# except ValueError:
#     print("only number!")

#dop kalkulator
# while True:
#     try:
#         num1 = int(input("first number:   "))
#         num2 = int(input("second number:   "))
#         operation = input("choose operation +,-,/,*:   ")
#         if operation == "+":
#             print(num1+num2)
#         elif operation == "-":
#             print(num1-num2)
#         elif operation == "/":
#             print(num1 / num2)
#         elif operation == "*":
#             print(num1 * num2)
#         # if input("ходните продолжить - да или - нет") == "да":
#         #     True
#         # else:
#         #     break
#     except ZeroDivisionError:
#         print("на ноль делить нельзя")
#     except ValueError:
#         print("введи корректные данные")
#     if input("ходните продолжить - да или - нет") == "да":
#         True
#     else:
#         break

# a =[]
# while True:
#     txt = input("write the text: ")
#     s = txt.split()a
#     b = len(s)
   
#     if b < 6:
#         print("pobolshe slov")
#         True
#     else:
#         a.append(txt)
#         print(a)
#         break
    
# a = 0, 0, 0, 0, 0
# for i in a:    
#     print(i)
    

a = 0
i = 1
while i < 101:
    i += a 
    i += 1     
    print(a)

