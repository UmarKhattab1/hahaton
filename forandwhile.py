#1
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# lang1 = 'go'
# for i in languages:
#     if i == lang1:
#         print('this languages is in list') 
#     else:
#         print('no')

#2
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages: 
#     if i == "php":
#         break
#     print(i)

#3
# a = 7
# i = 0
# while i < 5:
#     a = a * 5
#     print(a)
#     i += 1

#4
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for k,v in enumerate(languages):
#     print(k,v)

#5
# for i in range(-9,10):
#     print(10-abs(i),end ="")

    
#6
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# for i in range(2,len(names),2):
#     print(names[i], end = " ")

#7
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# for i in range(1,len(names),2):
#     print(names[i], end = " ")

#8
a = int(input('input a number: '))
for i in range(100, 1000):
    if i == a:
        print("trehznachnoe")
        break
    else:
        print('ne trehznachnoe')
        break
    
     
        