# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести 
# с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


# first = int(input("Enter the first number: \n"))
# amount = int(input("Enter the amount of elements: \n"))
# difference = int(input("Enter the difference: \n"))
# array = [first]
# for i in range(1, amount-1):
#     array.append(first + ((i-1) * difference))
# print(array)




# Задача 32: Определить индексы элементов массива (списка), значения 
# которых принадлежат заданному диапазону (т.е. не меньше заданного минимума 
# и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

# import random


# def define(arr, mi, ma):
#     res = []
#     for i in range(len(array)):
#         if arr[i] in range(mi, ma):
#             res.append(i)

#     return res
           

# size = int(input("Enter the length of the array: "))
# array = [random.randint(-999, 1000) for i in range(size)]
# print(array)
# min = int(input("Enter the minimal number of the range: "))
# max = int(input("Enter the maximal number of the range: "))
# print(f"The elements of the definde range have following indexes {define(array, min, max)}")