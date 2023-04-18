# Дан список чисел. Определите,
# сколько в нем встречается различных чисел.

# list_nums = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]
# print(len(set(list_nums)))

#
# numbers = [input() for i in range(6)] # сворачивание кода сначало что складываем, потом как складывается
# print(len(set(numbers)))

numbers =[] #пустой список
for i in  range(6):# в цикле собираем данные внутрь пустого списка
    numbers.append(input())

print(len(set(numbers))) # set выкинет дубликаты, len вычисляет количество элементов
