# file = open("text.txt",mode = "r", encoding="utf-8")
# for name in file:
#     if "Agil" in name:
#         print("yes")
#     else:
#         print("no")
# file = open("text.txt",mode = "r",encoding='utf-8')
# print(file.read())
# file.close()
# file = open("text.txt",mode = "r",encoding="utf-8")
# for name in file:
#     if "Agil" in name:
#         print(name)
#     else:
#         print("no")


# file =open("text.txt",mode = "r",encoding="utf-8")
# for k,v in enumerate(file,1):
#     print(k,v)

# file.close()

# file2 = open('new.txt',mode = "w",encoding="utf-8")
# file2.write("hello world\n")
# file2.write("привет мир\n")
# file2.write("good day")
# file2.close()

# file3 = open("new.txt",mode ="a",encoding="utf-8")
# file3.write("hello Agil")
# file3.write("!!!!")
# file3.close()

# login = input("введите свой логин:   ")
# password = input("введите свой пароль :   ")
# regis = open("name_pas.txt",mode="a",encoding="utf-8")
# regis.write("логин   " + login + "\n")
# regis.write("пароль   "+ password + "\n")
# regis.close()

# with open("ааа.txt", mode = "a",encoding="utf-8") as f:
#     f.write("как дела")

#1
# a = open("directories.txt", mode="w", encoding="utf-8")
# a.write("bin    dev   lib    libx32      mnt   root  snap  \nsys  varboot   etc   lib32  lost+found  opt   run   srv   \ntmpcdrom  home  lib64  media       proc  sbin  swapfile  usr")
# a.close()

#2
# login = input("enter your loggin: ")
# password = input("enter your password: ")

# user = open("user.txt", mode="a", encoding="utf-8")
# user.write("your login - " + login + "\n")
# user.write("your password - " + password)
# user.close()

#3
# a = open("text.txt", mode="r", encoding="utf-8")
# for i in a:
#     if "w" in i:
#         print("yes")
#     else:
#         print("no")
# a.close()

#4
# message = '''Python is a widely used high-level programming language for general-purpose
# programming, created by Guido van Rossum and first released in 1991. An interpreted
# language, Python has a design philosophy that emphasizes code readability (notably
# using whitespace indentation to delimit code blocks rather than curly brackets or
# keywords), and a syntax that allows programmers to express concepts in fewer lines of
# code than might be used in languages such as C++ or Java.'''
# a = open("next.txt",mode ="w",encoding="utf-8")
# a.write(message)
# a.close()

# b = open("next.txt",mode = "r",encoding="utf-8")
# c =(b.read().split())
# dada = []
# for i in c:
#     if "t" in i or "T" in i:
#         dada.append(i)
# print(dada)

#5
# a = open("database.txt", mode="w", encoding="utf-8")
# a.write("umar 123\nbeki  321\nbakr  456\nmaga  654")
# a.close()
# a = open("database.txt", mode="r", encoding="utf-8")
# b = (a.read().split())
# # print(b)


# login = input("enter your login: ")
# password = input("enter your password: ")

# for login in b: 
    
        
        
#     if login not in b or password not in b:
#         print("takogo polzovatila netu: ")
#         l = input("enter other login: ")
#         if l not in b:
#             p = input("enter new password: ")
#             p2 = input("repeat the password: ")
#             if p == p2:
                
#                 c = open("database.txt", mode="a", encoding="utf-8")
#                 c.write(f"\n{l}, {p2}")
#                 c.close()
#                 break    

#6
# login = input("enter the login: ")
# password = input("enter the password: ")
# photo = input()
