# Задача 2: Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 


num = int(input("Введите трехзначное число: "))

summ = num % 10
num = num // 10

summ = summ + num % 10
num = num // 10

summ = summ + num % 10

print ("Сумма цифр равна: ")
print (summ)
