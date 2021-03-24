# Задание 4.
# Создайте словарь характеристик продукта с ключами «title» (значение типа данных str),
# «price» (значение численного типа данных), «ingredients» (значение – список строк).
d = {'title': 'cocacola', 'price': 25, 'ingredients': ['ingredient_1', 'ingredient_2', 'ingredient_3']}

# 1.	Добавьте еще одну пару ключ-значение - «description»: какой-то текст
d['description'] = 'drink'
print(d)

# 2.	Увеличьте цену на 100.
d['price'] = d['price'] * 100
print(d)

# 3.	Добавьте в список ингредиентов еще один ингредиент.
x=d.get('ingredients')
x.append('qwerty')
print(d)

# 4.	Выведите на экран количество ингредиентов продукта.
print(len(d.get('ingredients')))

# 5.	Удалите из словаря значение с ключом «description»
del d['description']
print(d)
