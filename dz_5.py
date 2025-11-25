# Задача 1 (Создание словаря)
# Создай словарь с именем student, который содержит следующую информацию о студенте:
# Имя (ключ "name") — "Алексей"
# Возраст (ключ "age") — 20
# Город (ключ "city") — "Москва"
# Просто создай этот словарь. Выводить его на экран не нужно.

student = {
    "name": "Алексей",
    "age": 20,
    "city": "Москва"
}
print(student)

# Задача 2 (Доступ к элементам словаря по ключу)
# У тебя есть словарь:
# car = {"brand": "Toyota", "model": "Camry", "year": 2020}
# Выведи на экран значение, которое соответствует ключу "model".

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020
}
print(car["model"])

# Задача 3 (Добавление и обновление элементов словаря)
# У тебя есть словарь:
# fruit = {"name": "apple", "color": "red"}
# Добавь в этот словарь новый ключ "weight" со значением 150.
# Обнови значение ключа "color" на "green".
# В конце выведи получившийся словарь на экран.

fruit = {
    "name": "apple",
    "color": "red"
}
fruit["weight"] = 150
fruit["color"] = "green"
print(fruit)

# Задача 4 (Удаление элементов словаря)
# У тебя есть словарь:
# book = {"title": "Преступление и наказание", "author": "Достоевский", "year": 1866, "pages": 671}
# Удали из словаря элемент с ключом "pages" с помощью оператора del.
# В конце выведи получившийся словарь на экран.

book = {
    "title": "Преступление и наказание",
    "author": "Достоевский",
    "year": 1866,
    "pages": 671
}

del book["pages"]
print(book)

# Задача 5 (Проверка на наличие ключей и значений)
# У тебя есть словарь:
# pc = {"brand": "ASUS", "ram_gb": 16, "ssd": True}
# Проверь, есть ли в словаре ключ "ssd". Результат проверки (True или False) сохрани в переменную has_ssd.
# Проверь, есть ли в словаре значение "ASUS". Результат проверки (True или False) сохрани в переменную has_asus.
# В конце выведи на экран значения переменных has_ssd и has_asus.

pc = {
    "brand": "ASUS",
    "ram_gb": 16,
    "ssd": True
}

if "ssd" in pc:
    has_ssd = True
else:
    has_ssd = False
if "ASUS" in pc.values():
    has_asus = True
else:
    has_asus = False
print(has_ssd,has_asus)

# Задача 6 (Получение элементов, ключей и значений словаря)
# У тебя есть словарь:
# country = {"name": "Бразилия", "continent": "Южная Америка", "population": 214000000}
# Получи список всех ключей словаря и сохрани его в переменную keys_list.
# Получи список всех значений словаря и сохрани его в переменную values_list.
# В конце выведи на экран список ключей, а на следующей строке — список значений.

country = {
    "name": "Бразилия",
    "continent": "Южная Америка",
    "population": 214000000
}
keys_list = country.keys()
values_list = country.values()
print (list(keys_list))
print (list(values_list))

# Задача 7 (Доступ к элементам словаря по ключу)
# У тебя есть словарь:
# movie = {"title": "Криминальное чтиво", "director": "Квентин Тарантино", "year": 1994}
# Получи значение, которое соответствует ключу "director", и сохрани его в переменную director_name.
# Выведи на экран значение переменной director_name.

movie = {
    "title": "Криминальное чтиво",
    "director": "Квентин Тарантино",
    "year": 1994
}

director_name = movie["director"]
print(director_name)

# Задача 8 (Удаление элементов словаря)
# У тебя есть словарь:
# phone = {"brand": "Samsung", "model": "Galaxy S21", "os": "Android", "storage_gb": 128}
# Удали из словаря элемент с ключом "os" с помощью метода .pop().
# В конце выведи получившийся словарь на экран.

phone = {
    "brand": "Samsung",
    "model": "Galaxy S21",
    "os": "Android",
    "storage_gb": 128
}
result = phone.pop("os")
print(phone)

# Задача 9 (Создание словаря)
# Создай пустой словарь с именем shopping_cart. Затем добавь в него два элемента:
# Ключ "apple" со значением 3
# Ключ "milk" со значением 1
# Выведи получившийся словарь на экран.

shopping_cart = {
    "apple": 3,
    "milk": 1
}

print(shopping_cart)

# Задача 10 (Проверка на наличие ключей и значений)
# У тебя есть словарь:
# user = {"id": 101, "login": "super_user", "email": "super@mail.ru", "is_active": True}
# Проверь, есть ли в словаре ключ "phone". Результат проверки (True или False) сохрани в переменную has_phone.
# Проверь, присутствует ли в словаре значение True. Результат проверки (True или False) сохрани в переменную has_true.
# В конце выведи на экран значения переменных has_phone и has_true.

user = {
    "id": 101,
    "login": "super_user",
    "email": "super@mail.ru",
    "is_active": True
}
if "phone" in user:
    has_phone = True
else:
    has_phone = False
if True in user.values():
    has_true = True
else:
    has_true = False
print(has_phone,has_true)

# Задача 11

# Дан словарь colors = {"red": "красный", "blue": "синий", "green": "зеленый"}. Удали элемент с ключом "blue" из этого словаря.

colors = {
    "red": "красный",
    "blue": "синий",
    "green": "зеленый"
}

del colors["blue"]
print(colors)

# Задача 12
# Дан словарь book = {"title": "Война и мир", "author": "Толстой"}. Выведи на экран название книги, обратившись к ней по ключу.

book = {
    "title": "Война и мир",
    "author": "Толстой"
}

print(book["title"])

# Задача 13
# Дан словарь inventory = {"pens": 10, "pencils": 5}. Проверь, есть ли в словаре ключ "pens". Результат проверки (True или False) сохрани в переменную.

inventory = {
    "pens": 10,
    "pencils": 5
}
result = "pens" in inventory
print(result)

# Задача 14
# Дан словарь phone = {"model": "Galaxy"}. Обнови значение ключа "model" на "iPhone" и добавь новый ключ "year" со значением 2023.

phone = {
    "model": "Galaxy"
}
phone ["model"] = "iPhone"
phone["year"] = 2023
print(phone)

# Задача 15
# Дан словарь user = {"name": "Alice", "city": "London"}. Выведи на экран список всех ключей этого словаря.

user = {
    "name": "Alice",
    "city": "London"
}
print(user.keys())

# Задача 16
# Создай пустой словарь с названием car и добавь в него два элемента: ключ "brand" со значением "Toyota" и ключ "model" со значением "Camry".

car = {

}
car["brand"] = "Toyota"
car["model"] = "Camry"
print(car)

# Задача 17
# Дан словарь exam_results = {"math": 90, "science": 85}.
# Проверь, есть ли в словаре значение 85. Результат проверки (True или False) сохрани в переменную.

exam_results = {
    "math": 90, "science": 85
}
result = 85 in exam_results.values()
print(result)

# Задача 18
# Дан словарь temp_data = {"yesterday": 25, "today": 27, "tomorrow": 26}. Удали значение для вчерашнего дня ("yesterday").

temp_data = {
    "yesterday": 25,
    "today": 27,
    "tomorrow": 26
}

temp_data.pop("yesterday")
print(temp_data)

temp_data = {
    "yesterday": 25,
    "today": 27,
    "tomorrow": 26
}

del temp_data["yesterday"]
print(temp_data)

# Задача 19
# У тебя есть пустой словарь shopping_cart. Добавь в него товар: ключ "apple" со значением 5 (количество) и товар "milk" со значением 1.

shopping_cart = {

}
shopping_cart["apple"] = 5
shopping_cart["milk"] = 1
print(shopping_cart)

# Задача 20
# Дан словарь fruit_prices = {"apple": 0.5, "banana": 0.3}. Выведи на экран список всех значений этого словаря.

fruit_prices = {
    "apple": 0.5, "banana": 0.3
}
print(fruit_prices.values())

# Задача 21
# Дан словарь pc = {"cpu": "Intel", "ram_gb": 16}. Выведи на экран значение, связанное с ключом "ram_gb".

pc = {
    "cpu": "Intel",
    "ram_gb": 16
}

print(pc["ram_gb"])

# Задача 22
# Создай словарь с названием student, который будет содержать ключи "name" (твое имя) и "age" (твой возраст).

student = {
    "name": "Alena",
    "age": 29
}

print(student)