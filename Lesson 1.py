# print (5)
# n = 'bbbb'
# print(type(n))#выводит тип переменной

# n = 'fd\'hhh'-выводит ковычку
# print(n)

# a = 1
# d=2.89
# c='hello'
# print("{}-{}-{}".format(a,d,c)) ///выводит значение нескольких перемееных;
# ///{f}-,берет значение переменной f

# print('Введите первую строку')
# a = input()

# b = input('Введите второе число: ') ///-приглашение на ввод значения

# print('Введите первую строку')
# a = int(input())

# b = int(input('Введите второе число: '))
# print (a,' + ',b,' = ', a + b)

# n=int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток равен нулю
#         flag = False
#         print(i)
#     elif i > n // 2: # делить число без остатка
#         print(n)
#         flag = False
#     i+=1

# Можно сравнивать не только числовые значения, но и строки:
# a = 'qwe'
# b = 'qwe'
# print(a == b) # True

#В Python можно использовать тройные и даже четверные неравенства:
# a = 1 < 3 < 5 < 10
# print (a) # True

#Пример оформления программного кода с операторами ветвления:
# a = int(input("a = "))
# b = int(input("b = "))
# if a > b:
#     print(a)
# else:
#     print(b)

#Сложные условия
# n = int(input("n ="))
# if n % 2 == 0 and n % 3 == 0:
#     print('Число кратно 6')
# if n % 5 == 0 and n % 3 == 0:
#     print('Число кратно 15')

#Управляющие конструкции: while и вариация while-else
# n = 111
# summa = 0
# while summa > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa) # 9

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)

# n = 423
# summa = 0
# while summa > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(summa)
# Пожалуй
# хватит )
# 9

# Задача: Пользователь вводит число, необходимо найти минимальный делитель
# данного числа
# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
# i += 1

# Цикл for, range
# В Python цикл for в основном используется для перебора значений
# Пример использования цикла for:
# for i in 1, -2, 3, 14, 5:
#     print(i) # 1 -2 3 15 5

# Range
# ● Range выдает значения из диапазона с шагом 1.
# ● Если указано только одно число — от 0 до заданного числа.
# ● Если нужен другой шаг, третьим аргументов можно задать приращение.
# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(-5, 0) # ----
# r = range(1, 10, 2) # 1 3 5 7
# r = range(100, 0, -20) # 100 80 60 40 20
# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
#     print(i)
# 100 80 60 40 20

# for i in range(5):
#     print(i)
# # 0 1 2 3 4

# for i in 'qwerty':
#     print(i)

# Можно использовать вложенные циклы:
# line = ""
# for i in range(5):
#     line = ""
# for j in range(5):
#     line += "*"
# print(line)




