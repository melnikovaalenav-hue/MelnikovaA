# Задача 1 (раздел: Конструктор класса init)
# Создайте класс Book.
# В конструкторе класса (__init__) определите три атрибута: title (название), author (автор) и pages (количество страниц).
# Атрибуты должны инициализироваться значениями, переданными при создании объекта.
# Пример создания объекта после того, как класс будет готов:
# my_book = Book("1984", "George Orwell", 328)
# Напишите код класса.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

my_book = Book("1984","George Orwell", 328)


# Задача 2 (раздел: Методы класса)
# Создайте класс Calculator.
# Добавьте в класс метод add, который принимает два числа (кроме self) и возвращает их сумму.
# Пример использования после того, как класс будет готов:
# my_calc = Calculator()
# result = my_calc.add(5, 3)
# print(result) # Должно вывести 8
# Напишите код класса с методом add.

class Calculator:
    def add(self, num1, num2):
        resalt = (num1 + num2)
        return resalt

my_calc = Calculator()
print(my_calc.add(5,3))

# Задача 3 (раздел: Общие атрибуты)
# Создайте класс Employee.
# Добавьте в класс общий атрибут company со значением "TechCorp". Этот атрибут должен принадлежать классу, а не отдельным объектам.
# В конструкторе инициализируйте атрибут name (имя сотрудника) для каждого объекта.
# Создайте два объекта:
# emp1 = Employee("Alice")
# emp2 = Employee("Bob")
# После этого выведите значение company для каждого объекта (например, print(emp1.company)).
# Напишите код класса Employee.

class Employee:
    COMPANY = "TechCorp"

    def __init__(self, name):
        self.name = name

emp1 = Employee("Alice")
emp2 = Employee("Bob")
print(emp1.COMPANY)
print(emp2.COMPANY)

# Задача 4 (раздел: Понимание параметра self)
# Создайте класс Car.
# В конструкторе инициализируйте атрибут brand (марка автомобиля) для объекта.
# Добавьте метод show_brand, который печатает значение brand для этого автомобиля. Внутри метода обращайтесь к атрибуту через self.
# Пример использования после того, как класс будет готов:
# my_car = Car("Toyota")
# my_car.show_brand() # Должно вывести: Toyota
# Напишите код класса Car.

class Car:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(self.brand)

my_car = Car("Toyota")
my_car.show_brand()

# Задача 5 (раздел: Создание класса и объект класса)
# Создайте простой класс Dog.
# Внутри класса определите только один атрибут species со строковым значением "Canis familiaris" (это общий атрибут класса, не в конструкторе).
# Затем создайте объект этого класса с именем my_dog и выведите значение атрибута species этого объекта.
# Напишите код класса Dog и создание объекта.

class Dog:
    SPECIES = "Canis familiaris"

my_dog = Dog()
print(my_dog.SPECIES)

# Задача 6 (раздел: Введение в ООП / базовый синтаксис)
# Создайте класс Point, который представляет точку на плоскости.
# В конструкторе инициализируйте два атрибута: x и y (координаты точки).
# Затем создайте объект point1 с координатами (3, 5) и выведите его атрибуты вручную (например, print(point1.x, point1.y)).
# Напишите код класса Point и создание объекта с выводом.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point1 = Point(3, 5)
print(point1.x, point1.y)

# Задача 7 (комбинированная, на закрепление ООП)
# Создайте класс BankAccount, который имитирует простой банковский счёт.
# Класс должен содержать:
# Общий атрибут класса bank_name со значением "Digital Bank".
# Конструктор __init__, который принимает account_holder (владелец счёта, строка) и balance (баланс, число).
# Конструктор инициализирует атрибуты holder и balance для объекта.
# Метод deposit(amount), который увеличивает баланс на указанную сумму amount и печатает сообщение:
# "Пополнение на {amount}. Новый баланс: {self.balance}".
# Метод withdraw(amount), который уменьшает баланс на указанную сумму amount, но только если на счету достаточно средств.
# Если достаточно, то производит списание и печатает: "Снятие {amount}. Новый баланс: {self.balance}".
# Если недостаточно, печатает: "Недостаточно средств. Текущий баланс: {self.balance}".
# Метод display_info(), который печатает информацию в формате:

class BankAccount:
    BANK_NAME = "Digital Bank"

    def __init__(self, account_holder, balance):
        self.holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"Пополнение на {amount}. Новый баланс: {self.balance}")
    def withdraw(self,amount):
            if self.balance >= amount:
                self.balance -= amount
                print(f"Снятие {amount}. Новый баланс: {self.balance}")
            else:
             print(f"Недостаточно средств. Текущий баланс: {self.balance}")
    def display_info(self):
        print( f"Bank: {self.BANK_NAME}\nHolder: {self.holder}\nBalance: {self.balance}")

acc1 = BankAccount("Иванов Иван", 1000)
acc1.deposit(101)
acc1.withdraw(560)
acc1.display_info()

# Задача 8 (повторение и комбинирование)
# Создайте класс Student, который представляет студента.
# Требования:
# Общий атрибут класса university со значением "National University".
# Конструктор принимает name (имя студента) и student_id (номер студенческого билета). Инициализирует атрибуты name и student_id объекта.
# Метод add_grade(self, subject, grade) – добавляет оценку по предмету.
# Предметы и оценки храните в словаре self.grades, где ключ – название предмета (строка), значение – оценка (целое число). Если словаря ещё нет,
# создайте его в конструкторе (или при первом добавлении). Метод должен обновлять словарь и печатать: "Добавлена оценка {grade} по предмету {subject}".
# Метод get_average(self) – возвращает средний балл студента по всем предметам (округлить до двух знаков после запятой). Если оценок нет, возвращает 0.
# Метод show_info(self) – выводит информацию в формате:
# text
# Student: {self.name}
# ID: {self.student_id}
# University: {self.university}
# Grades: {self.grades}
# Average: {средний балл}

class Student:
    UNIVERSITY = "National University"
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}
    def add_grade(self, subject, grade):
        self.grades[subject] = grade
        print(f"Добавлена оценка {grade} по предмету {subject}")
    def get_average(self):
        if not self.grades:
            return 0
        else:
            return  round(sum(self.grades.values()) / len(self.grades.keys()), 2) # round() округляет число до указанного количества знаков после запятой
            # синтаксис round(number, ndigits) -number: число, которое нужно округлить.
            # ndigits: необязательный аргумент, указывающий количество знаков после запятой. Если его не указать, округляет до ближайшего целого.
    def show_info(self):
        print(f"Student: {self.name}\nID: {self.student_id}\nUniversity: {self.UNIVERSITY}\nGrades: {self.grades}\nAverage: {self.get_average()}")

student1 = Student("Петров Василий", 1)
student1.add_grade("Математика",4)
student1.add_grade("Литература",5)
student1.get_average()
student1.show_info()

student2 = Student("Иванов Василий", 2)
student2.add_grade("Русский язык",3)
student2.get_average()
student2.show_info()

# Задача 9 (раздел: Создание класса и объект класса)
# Создайте класс Robot.
# Внутри класса определите только один атрибут category со строковым значением "Artificial Intelligence" (это общий атрибут класса).
# Затем создайте объект этого класса с именем my_robot и выведите значение атрибута category этого объекта.
# Напишите код класса Robot и создание объекта с выводом.

class Robot:
    CATEGORY = "Artificial Intelligence"

robot1= Robot()
print(robot1.CATEGORY)

# Задача 10 (раздел: Конструктор класса init)
# Создайте класс Laptop.
# В конструкторе класса (__init__) определите два атрибута:
# brand (бренд ноутбука) и price (цена). Атрибуты должны инициализироваться значениями, переданными при создании объекта.
# Пример создания объекта после того, как класс будет готов:
# my_laptop = Laptop("Dell", 75000)
# Напишите код класса Laptop.

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

my_laptop = Laptop("Dell", 75000)
print(my_laptop.brand, my_laptop.price)

# Задача 11 (раздел: Общие атрибуты)
# Создайте класс MobilePhone.
# Добавьте в класс общий атрибут os со значением "Android". Этот атрибут должен принадлежать классу, а не отдельным объектам.
# В конструкторе инициализируйте атрибут model (модель телефона) для каждого объекта.
# Создайте два объекта:
# phone1 = MobilePhone("Samsung Galaxy")
# phone2 = MobilePhone("Google Pixel")
# После этого выведите значение os для каждого объекта (например, print(phone1.os)).
# Напишите код класса MobilePhone.

class MobilePhone:
    OS = "Android"

    def __init__(self, model):
        self.model = model

phone1 = MobilePhone("Samsung Galaxy")
phone2 = MobilePhone("Google Pixel")
print(phone1.OS)
print(phone2.OS)

# Задача 12 (раздел: Понимание параметра self)
# Создайте класс TemperatureSensor.
# В конструкторе инициализируйте атрибут current_temp (текущая температура) для объекта.
# Добавьте метод display_temp, который печатает значение current_temp в формате:
# "Текущая температура: {self.current_temp}°C".
# Внутри метода обращайтесь к атрибуту через self.
# Пример использования после того, как класс будет готов:
# sensor = TemperatureSensor(25.5)
# sensor.display_temp() # Должно вывести: Текущая температура: 25.5°C
# Напишите код класса TemperatureSensor.

class TemperatureSensor:
    def __init__(self, current_temp):
        self.current_temp = current_temp

    def display_temp(self):
        print(f"Текущая температура: {self.current_temp}°C")

sensor = TemperatureSensor(25.5)
sensor.display_temp()

# Задача 13 (раздел: Методы класса)
# Создайте класс MathHelper.
# Добавьте в класс метод multiply, который принимает два числа (кроме self) и возвращает их произведение.
# Пример использования после того, как класс будет готов:
# helper = MathHelper()
# result = helper.multiply(4, 7)
# print(result) # Должно вывести 28
# Напишите код класса с методом multiply.

class MathHelper:

    def multiply(self, num1, number2):
        return num1 * number2
helper = MathHelper()
result = helper.multiply(4 ,7)
print(result)

# Задача 14 (раздел: Создание класса)
# Создайте пустой класс EmptyClass без атрибутов и методов.
# Затем создайте объект этого класса с именем empty_obj.
# Напишите код класса и создание объекта.

# class EmptyClass:

# empty_obj = EmptyClass()

# Задача 15 (раздел: Объект класса)
# Создайте класс Flashlight с конструктором __init__, который инициализирует атрибут color (цвет фонарика) для объекта.
# Создайте два объекта этого класса:
# flash1 = Flashlight("красный")
# flash2 = Flashlight("синий")
# Затем выведите атрибут color каждого объекта.
# Напишите код класса Flashlight и создание объектов с выводом.

class Flashlight:
    def __init__ (self, color):
        self.color = color

flash1 = Flashlight("красный")
flash2 = Flashlight("синий")
print(flash1.color)
print(flash2.color, flash1.color)










