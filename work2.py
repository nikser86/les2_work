# Задание 2

# 1.	Вычислите длину гипотенузы в прямоугольном треугольнике со сторонами 367 и 127.
import math

a = math.sqrt((367 ** 2) + (127 ** 2))
print(a)

# 2.	Дано двузначное число. Найдите число десятков в нем.
a = 82 // 10
print(a)

# 3.	Дано трёхзначное число. Найдите сумму его цифр.
a = 456
z = ((a // 10) // 10) + ((a // 10) % 10) + (a % 10)
print(z)

# 4.	Дано целое число n. Выведите следующее за ним чётное число.
a = 11
print(a // 2 * 2 + 2)

# 5.	Дано положительное действительное число X. Выведите его дробную часть.
a = 23.23
print(a % 1)

# 6.	Дано положительное действительное число X. Выведите его первую цифру после десятичной точки.
a = 321314.4567
print(round((a % 1 * 100) // 10))
s = str(a)
print(s[s.find('.')+1])