# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

i = int (input('Введите номер билета: '))
k = i // 1000
m = i % 1000
summa = 0
while k > 0:
    x = k % 10
    summa = summa + x
    k = k// 10
print(summa)
summa1 = 0
while m > 0:
    x = m % 10
    summa1 = summa1 + x
    m = m// 10
print(summa1)
if summa1 == summa:
    print('Ура, счастливый билет')
else:
    print('Повезет в следующий раз')

