#Задача 1 ---------------------------------------------
'''
class Person:
    def __init__(self, name, age, phone, brand, yer):
        self.name = name
        self.age = age
        self.phone = phone
        #self.brand = brand
        #self.yer = yer
    def get_info(self):
        return f"Имя: {self.name}\nВозраст: {self.age}\nТелефон: {self.phone}"
person1 = Person("Вика", 18, "+7 747 369 85 21")
person2 = Person("Арман", 22, "+7 747 348 89 86")
#person3 = Person("ipone 12", 2025)
#person4 = Person("")
print("Информация о первом человеке:")
print(person1.get_info())
print("\nИнформация о втором человеке:")
print(person2.get_info())
'''
#Задача 2 канкулятор ---------------------------------------------
'''
class Calculator:
    def add(self, a, b):
        return a + b
    def multiply(self, a, b):
        return a * b
calc = Calculator()
sum_result = calc.add(2, 3)
product_result = calc.multiply(4, 5)
print("Результат сложения: 2 + 3 =", sum_result)
print("Результат умножения: 4 * 5 =", product_result)
'''
#----------------------------------------------------------
'''
Объектно-ориентированное программирование
- Классы и объекты
'''
#----------------------------------------------------------
#Задача 3.1.1 ---------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
'''
Упражнение 1

Определите класс Rectangle, который представляет прямоугольник.
Через конструктор класс принимает ширину и длину и сохраняет их в атрибутах width и length соответственно.
Также этом классе определите метод area,
который возвращает площадь прямоугольника, и метод perimeter,
который возвращает периметра прямоугольника.

После создания класса определите несколько объектов класса Rectangle и продемонстрируйте работу его методов.
'''
#---------------------------------------------------------------------------------------------------------------------
'''
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area(self):
        return self.width * self.length
    def perimeter(self):
        return 2 * (self.width + self.length)
rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)
rect3 = Rectangle(8, 4)
print(f"Прямоугольник 1: ширина={rect1.width}, длина={rect1.length}")
print(f"Площадь: {rect1.area()}")
print(f"Периметр: {rect1.perimeter()}")
print("\nПрямоугольник 2: ширина={0}, длина={1}".format(rect2.width, rect2.length))
print(f"Площадь: {rect2.area()}")
print(f"Периметр: {rect2.perimeter()}")
print(f"\nПрямоугольник 3: ширина={rect3.width}, длина={rect3.length}")
print(f"Площадь: {rect3.area()}")
print(f"Периметр: {rect3.perimeter()}")
'''
#Задача 4.1.2 ---------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
'''
Упражнение 2
Создайте класс BankAccount, который представляет банковский счет.
Определите в этом классе атрибуты account_number и balance, которые представляют номер счета и баланс.
Через параметры конструктора передайте этим атрибутам начальные значения.

Также в классе определите метод add, который принимает некоторую сумму и добавляет ее на баланс счета.
И определите метод withdraw, который принимает некоторую сумму и снимает ее с баланса.
При этом с баланса нельзя снять больше, чем имеется.
Если на балансе недостаточно средств, то пользователю должно выводиться соответствующее сообщение.
'''
#---------------------------------------------------------------------------------------------------------------------
'''
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    def add(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"На счет {self.account_number} добавлено {amount}. Новый баланс: {self.balance}")
        else:
            print("Сумма для пополнения должна быть положительной.")
    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма для снятия должна быть положительной.")
        elif amount > self.balance:
            print("Недостаточно средств на счете.")
        else:
            self.balance -= amount
            print(f"Снято {amount} со счета {self.account_number}. Остаток: {self.balance}")
account = BankAccount("1234567890", 1000)
account.add(500)
account.withdraw(200)
account.withdraw(1500)
account.add(-50)
account.withdraw(-100)
'''
#чероновик_испытание_моего_кода ---------------------------------------------
'''
import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(100000)
pygame.quit()
'''
#---------------------------------------------------------------------------------------------------------------------
'''
class Person:

    def __init__(self, name):
        self.__name = name  # имя человека

    @property
    def name(self):
        return self.__name

    def do_nothing(self):
        print(f"{self.name} does nothing")


#  класс работника
class Employee(Person):

    def work(self):
        print(f"{self.name} works")


#  класс студента
class Student(Person):

    def study(self):
        print(f"{self.name} studies")


def act(person):
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Employee):
        person.work()
    elif isinstance(person, Person):
        person.do_nothing()


tom = Employee("Tom")
bob = Student("Bob")
sam = Person("Sam")

act(tom)  # Tom works
act(bob)  # Bob studies
act(sam)  # Sam does nothing
'''