# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

array_length = int(input('Введите количество элементов в массиве: '))
array = [randint(1, 20) for _ in range(array_length)]
print(array)
number = int(float(input('Введите чиcло X: ')))
x_max = 20
for i in array:    
    if abs(i - number) < x_max:
        x_max = abs(i - number)
        numb = i
print(f'Самый близкий по величине элемент  к заданному числу - {numb}')
