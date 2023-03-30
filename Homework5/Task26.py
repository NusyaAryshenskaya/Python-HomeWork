# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

a = int(input("Введите число: "))
b = int(input("Введите степень числа: "))

def power(a, b):
    if b == 1:
        return a
    return power(a, b - 1)*a


print(f"Число {a} в степени {b} => {power(a, b)}")