# Задание 1
# (Подсказка: ищите как это сделать с помощью методов строк)
# 1.	Определите является ли строка записью числа. (Подсказка: ищите как это сделать с помощью методов строк)
s = '1234123454634563456'
print(s.isdigit())

# 2.	Посчитайте сколько у вас пробелов в строке.
s = 'asdf wqer qwer '
print(s.count(' '))

# 3.	Посчитайте сколько у вас символов точки '.' в строке.
print(s.count('.'))

# 4.	Создайте строку "Homework". Преобразуйте её в строку длиной 100 символов,
# посередине которой исходное слово, а с обоих сторон строка заполнена пробелами.
# Выведите её на экран. Убедитесь, что у вас 100 символов (посчитайте длину).
s = "Homework"
s = s.center(100)
print(s)
print(s.__len__())

# 5.	Сделайте первые буквы слов строки большими (upper case).
s = 'asdf dfgh ghj rtuy'
s = s.title()
print(s)

# 6.	Определите заканчивается ли ваша строка подстрокой “ing”.
s = 'xzcvzxcvzxcvzxcv xzcv zxc ing'
print(s.endswith('ing'))

# 7.	Определите индекс первого вхождения символа “a” в вашей строке.
s = 'dsfdsadsafdfasdfasdf'
print(s.index('a'))

# 8.	Разбейте строку на список подстрок по символу пробела.
s = 'asdfasdfas asdf asdffghj fgjfg jhfghjghj'
s.split(' ')
print(s)

# 9.	Пусть у вас строка имеет пробельные символы. Найдите метод,
# который удаляет пробельные символы вначале и в конце, но не посередине.
s='   asdfasdf asdf asd fasdfasdf    '
print(s.strip())