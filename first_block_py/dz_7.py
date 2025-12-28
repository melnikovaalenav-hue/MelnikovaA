from itertools import count

# Задача 1
# Создай новый текстовый файл с именем my_file.txt. Запиши в него одну строку: Hello, Python!.
# (Для этой задачи используй контекстный менеджер with).

with open("../my_file.txt", "a+", encoding="utf-8") as file:
    file.write("Пока, Python!")
    file.seek(0)
    print(file.read())

# Задача 2
# Прочитай содержимое файла example.txt и выведи его построчно в консоль. Предполагается, что файл уже существует.

with open ("../my_file.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Задача 3
# Добавь в конец существующего файла notes.txt новую строку: Это новая запись..

with open("../my_file.txt", "a+", encoding="utf-8") as file:
    file.write( "\nЭто новая запись..")
    file.seek(0)
    print(file.read())

# Задача 4
# Создай файл numbers.txt и запиши в него числа от 1 до 5, каждое с новой строки.

with open("../numbers.txt", "w+", encoding="utf-8") as file:
    file.write("1\n2\n3\n4\n5")
    file.seek(0)
    print(file.read())

# Задача 5
# Прочитай файл list.txt и выведи только первую строку из него. Предполагается, что файл существует и содержит как минимум одну строку.

with open("../my_file.txt", "r", encoding="utf-8") as file:
        print(file.readline())

# Задача 6
# Создай пустой файл с именем empty.txt.
# (Для этой задача используй контекстный менеджер with).

with open ("../empty.txt", "w+", encoding="utf-8") as file:
    print("empty.txt")

# Задача 7
# Допиши в существующий файл log.txt текущую дату и время, каждое с новой строки. Используй модуль datetime для получения текущей даты и времени.

import datetime
with open ("../empty.txt", "a+", encoding="utf-8") as file:
    file.write(str(datetime.datetime.now()))
    file.seek(0)
    print(file.read())

# Задача 8
# Создай файл products.txt и запиши в него три продукта, каждый с новой строки: Яблоко, Банан, Апельсин.

with open ("../products.txt", "w+", encoding="utf-8") as file:
    file.write("Яблоко\nБанан\nАпельсин")
    file.seek(0)
    print(file.read())

# Задача 9
# Прочитай файл data.txt и выведи количество строк в этом файле. Предполагается, что файл существует.

with open ("../products.txt", "r+", encoding="utf-8") as file:
    count = len(file.readlines())
    print(count)

# Задача 10
# Создай файл info.txt, запиши в него одну строку: Файл создан!, затем переименуй его в information.txt.

import os
with open ("info.txt", "w+",encoding="utf-8") as file:
    file.write("Файл создан!")
os.rename("info.txt", "../information.txt")

