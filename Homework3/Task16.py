# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# Пример: # 5
#            1 2 3 4 5
#            3
#            -> 1
import random

array_length = int(input("Введите колличество элементов в массиве: "))
my_array = [random.randint(0, 10) for i in range(array_length)]
print(my_array)

number = int(input("Введите число X, его нужно найти: "))

count = 0
for i in range(array_length):
    if my_array[i] == number:
        count += 1

print(f"Число X встречается {count} раз(а)")