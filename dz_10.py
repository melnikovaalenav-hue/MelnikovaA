# Задача №1
# Создайте базовый (родительский) класс Animal. Внутри него определите:
# Метод __init__, который принимает параметр name (кличка животного) и сохраняет его в атрибут self.name.
# Метод make_sound, который печатает строку: "Животное издает какой-то звук".
# Затем создайте дочерний класс Dog, который наследуется от Animal.
# В классе Dog переопределите метод make_sound, чтобы он печатал строку: "{self.name} говорит: Гав!"
# Не нужно писать код для создания экземпляров или вывода. Создайте только сами классы Animal и Dog.

class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print("Животное издает какой-то звук")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} говорит: Гав!")

dog1 = Dog("Бобик")
dog1.make_sound()

# Задача №2
# Создайте базовый класс Vehicle (Транспортное средство). Внутри него определите:
# Метод __init__, который принимает параметр brand (марка) и сохраняет его в атрибут self.brand.
# Метод show_info, который возвращает (используйте return) строку: f"Транспортное средство: {self.brand}".
# Затем создайте дочерний класс Car, который наследуется от Vehicle.
# В методе __init__ класса Car должен приниматься еще один параметр — model (модель).
# Внутри __init__ класса Car с помощью super() вызовите метод __init__ родительского класса, чтобы правильно установить атрибут brand.
# После этого в том же __init__ сохраните параметр model в атрибут self.model.
# В классе Car переопределите метод show_info, чтобы он возвращал строку: f"Автомобиль: {self.brand} {self.model}".
# Создайте только сами классы Vehicle и Car.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def show_info(self):
        return f"Транспортное средство: {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def show_info(self):
        return f"Автомобиль: {self.brand} {self.model}"

my_auto = Car("BMV", "M5")
print(my_auto.show_info())

# Задача №3
# Создайте базовый класс Person. Внутри него определите:
# Метод __init__, который принимает параметры name (имя) и age (возраст) и сохраняет их в атрибуты self.name и self.age.
# Метод introduce, который печатает (используйте print) строку: "Меня зовут {self.name}, мне {self.age} лет.".
# Затем создайте дочерний класс Student, который наследуется от Person.
# В методе __init__ класса Student должен приниматься еще один параметр — student_id (номер студенческого билета).
# Внутри __init__ класса Student с помощью super() вызовите метод __init__ родительского класса, чтобы установить атрибуты name и age.
# После этого сохраните параметр student_id в атрибут self.student_id.
# Не переопределяйте метод introduce в классе Student. Он должен использоваться как есть из родительского класса.
# Создайте только сами классы Person и Student.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет.")

class Student(Person):
    def __init__(self, student_id, name, age):
        super().__init__(name, age)
        self.student_id = student_id

my_person = Student(3, "Алена", 28)
my_person.introduce()

# Задача №4
# Создайте базовый класс Book. Внутри него определите:
# Метод __init__, который принимает параметры title (название) и author (автор) и сохраняет их в атрибуты self.title и self.author.
# Метод get_info, который возвращает (используйте return) строку: f"'{self.title}' by {self.author}".
# Затем создайте дочерний класс EBook, который наследуется от Book.
# В методе __init__ класса EBook должен приниматься еще один параметр — file_size (размер файла в мегабайтах, целое число).
# Внутри __init__ класса EBook с помощью super() вызовите метод __init__ родительского класса, чтобы установить атрибуты title и author.
# После этого сохраните параметр file_size в атрибут self.file_size.
# В классе EBook переопределите метод get_info.
# Он должен возвращать строку от родительского метода get_info с добавлением в конце текста: " | File size: {self.file_size}MB".
# Подсказка: В переопределенном методе get_info класса EBook вам нужно получить
# результат работы родительского метода и добавить к нему свою часть строки.
# Создайте только сами классы Book и EBook.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        return f"'{self.title}' by {self.author}"

class EBook(Book):
    def __init__(self, file_size,title, author):
        super().__init__(title, author)
        self.file_size = file_size
    def get_info(self):
        return f"{Book.get_info(self)} | File size: {self.file_size}MB"

my_book = EBook(365, "Война и мир","Толстой")
print(my_book.get_info())

# Задача №5
# Создайте простую иерархию классов, представляющих разные типы сотрудников компании.
# Создайте базовый класс Employee. Внутри него определите:
# Метод __init__, который принимает параметр name (имя сотрудника) и сохраняет его в атрибут self.name.
# Метод get_role, который возвращает (используйте return) строку: "Сотрудник".
# Создайте дочерний класс Manager, который наследуется от Employee.
# В классе Manager переопределите метод get_role, чтобы он возвращал строку: "Менеджер".
# Создайте еще один дочерний класс Developer, который также наследуется от Employee.
# В классе Developer переопределите метод get_role, чтобы он возвращал строку: "Разработчик".
# Создайте только саму иерархию классов: Employee, Manager и Developer. Не нужно писать код для создания экземпляров.

class Employee:
    def __init__(self, name):
        self.name = name
    def get_role(self):
        return "Сотрудник"

class Manager(Employee):
    def get_role(self):
        return "Менеджер"

class Developer(Employee):
    def get_role(self):
        return "Разработчик"

result1 = Manager("Alex")
print(result1.get_role())
result2 = Developer("Anna")
print(result2.get_role())
