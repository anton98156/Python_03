# Seminar 3

# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# import os
# os.system("clear")

# list1 = ["2", "43", "5", "331", "91", "35", "79", "53"]
# x = input("Введите число: ")

# print(x in list1)

# for i in list1:
#     if x == i:
#         print(f"число {i} присутствует в списке")
#         break
# else:
#     print("заданное число отсутствует в списке")

# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# import os
# os.system("clear")

# my_list= ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# print(my_list)

# x = str(input("введите строку: "))

# string_find = x
# count = 0
# for i in range(len(my_list)):
#     if string_find == my_list[i]:
#         count+=1
#         if count == 2:
#             print(i)
#             break
# else:
#     print("нет")




# Home Work

# 1 Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import os
# os.system("clear")

# from random import randint

# list_1 = []
# for i in range(4):
#     list_1.append(randint(1,10))

# print(f"Дан список чисел: {list_1}")

# def count_odd():
#     sum = 0
#     for i in list_1:
#         if i % 2 > 0:
#             sum = sum + i
#     return sum

# a = count_odd()
# print(a)

# 2 Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# import os
# os.system("clear")
# from random import randint

# list_1 = []
# for i in range(4):
#     list_1.append(randint(1,10))

# print(f"Список: {list_1}")
# print(f"Произведение пары числе списка = [{list_1[0] * list_1[3]}, {list_1[1] * list_1[2]}]")

# if list_1[x/2]
# list_1[0] * list_1[x-1]

# 3 Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import os
# os.system("clear")

# import random

# list_1 = []
# for i in range(3):
#     list_1.append(round(random.uniform(1, 20), 2))

# print(f"Список: {list_1}")


# list_2 = list_1
# list_2[0] = round(list_2[0] % 1, 2)
# list_2[1] = round(list_2[1] % 1, 2)
# list_2[2] = round(list_2[2] % 1, 2)

# max = 0
# for i in list_2:
#     if max < i:
#         max = i
# max = max % 1


# min = list_2[0]
# if list_2[0] < list_2[1]:
#     min = list_2[0]
# else:
#     min = list_2[1]
# if min < list_2[2]:
#     min = min
# else:
#      min = list_2[2]
# min = min % 1

# print(f"Разница между максимальным и минимальным значением дробной части элементов = {round(max - min, 3)}")

# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# import os
# os.system("clear")

# z = int(input("Введите десятичное число: "))
# x = z
# list_1 = []
# while x >= 1:
#     a = x % 2
#     list_1 = [a] + list_1
#     x = x / 2
#     x = int(x)
# print(f'Десятичное число "{z}" преобразовано в двочиное: {list_1}')

# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# (ссылка на плтаформе)

import os
os.system("clear")

x = int(input("Введите число: "))

def find_f():
    list_1 = [0, 1]
    count = 2
    a = 0
    while count != x + 1:
        a = list_1[count - 1] + list_1[count - 2]
        list_1 = list_1 + [a]
        count = count + 1
    return list_1

list_f = find_f()
def find_f2():
    list_2 = list_f
    for index, item in enumerate(list_2):
        list_2[index] = -list_2[index]
    list_3 = list(reversed(list_2))
    del list_3[index - 0]
    return list_3

list_f2 = find_f2()
list_f3 = find_f()
list_rez = list_f2 + list_f3
print(list_rez)