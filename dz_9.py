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





