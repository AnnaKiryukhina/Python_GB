# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
import math
S = int (input('Введите произведение: '))
P = int (input('Введите сумму: '))
D = P * P - 4*S
x = (P + math.sqrt (D))/2
y = P - x
print(x)
print(y)