#q = int(input("ведите количество элементов списка: "))
#s = input("ведите первое число в список: ")
#print(q, s)
#средное аревмитическое
#посчитать их сумму
#мимнимум значение, максимум значение
#посчитать сколько отрицательные числа
#напиши программу в пайтон код нужно посчитать их сумму и средное аревмитическое
#выводите ваш список в обратном парятком
#нужно удалить четные числа
#взять число какойнибуть многозначное и посчитать сумму его цифр

#Задание_1-------------------------------------------------------
'''
for number = 0
while number < 9:
    print(f"number = {number}")
    number += 1
print("Работа программы завершена")
'''
#---------------------------------------------------------------
'''
q = int(input("ведите количество элементов списка: "))
sp=[]
for n in range(1, q + 1):
    input(f"ведите {n} число в список: ")
'''
#---------------------------------------------------------------
'''
q = int(input("Введите количество элементов списка: "))
sp = []
for n in range(1, q + 1):
    num = int(input(f"Введите {n}-е число в список: "))
    sp.append(num)
total = sum(sp)
print("\nСписок чисел:", sp)
print("Сумма всех чисел в списке:", total)
'''
#---------------------------------------------------------------
'''
q = int(input("Введите количество элементов списка: "))
sp = []
for n in range(1, q + 1):
    num = float(input(f"Введите {n}-е число в список: "))
    sp.append(num)
total = sum(sp)
average = total / len(sp) if sp else 0
print("\nСписок чисел:", sp)
print("Сумма чисел:", total)
print("Среднее арифметическое:", average)
'''
#---------------------------------------------------------------
'''
q = int(input("Введите количество элементов списка: "))
sp = []
for n in range(1, q + 1):
    num = float(input(f"Введите {n}-е число в список: "))
    sp.append(num)
total = sum(sp)
average = total / len(sp) if sp else 0
minimum = min(sp)
maximum = max(sp)
print("\nСписок чисел:", sp)
print("Сумма чисел:", total)
print("Среднее арифметическое:", average)
print("Минимальное значение:", minimum)
print("Максимальное значение:", maximum)
'''
#---------------------------------------------------------------
'''
q = int(input("Введите количество элементов списка: "))
sp = []
for n in range(1, q + 1):
    num = float(input(f"Введите {n}-е число в список: "))
    sp.append(num)
total = sum(sp)
average = total / len(sp) if sp else 0
minimum = min(sp)
maximum = max(sp)
negative_count = sum(1 for x in sp if x < 0)
print("\nСписок чисел:", sp)
print("Сумма чисел:", total)
print("Среднее арифметическое:", average)
print("Минимальное значение:", minimum)
print("Максимальное значение:", maximum)
print("Количество отрицательных чисел:", negative_count)
'''
#---------------------------------------------------------------
'''
q = int(input("Введите количество элементов списка: "))
sp = []
for n in range(1, q + 1):
    num = float(input(f"Введите {n}-е число в список: "))
    sp.append(num)
total = sum(sp)
average = total / len(sp) if sp else 0
minimum = min(sp)
maximum = max(sp)
negative_count = sum(1 for x in sp if x < 0)
print("\nСписок чисел:", sp)
print("Список в обратном порядке:", list(reversed(sp)))
print("Сумма чисел:", total)
print("Среднее арифметическое:", average)
print("Минимальное значение:", minimum)
print("Максимальное значение:", maximum)
print("Количество отрицательных чисел:", negative_count)
print("Список в обратном порядке:", list(reversed(sp)))
'''
#---------------------------------------------------------------
'''
q = int(input("Введите количество элементов списка: "))
sp = []
for n in range(1, q + 1):
    num = float(input(f"Введите {n}-е число в список: "))
    sp.append(num)
sp = [x for x in sp if not (x % 2 == 0 and x == int(x))]
total = sum(sp)
average = total / len(sp) if sp else 0
minimum = min(sp) if sp else None
maximum = max(sp) if sp else None
negative_count = sum(1 for x in sp if x < 0)
print("\nСписок чисел (после удаления чётных):", sp)
print("Список в обратном порядке:", list(reversed(sp)))
print("Сумма чисел:", total)
print("Среднее арифметическое:", average)
print("Минимальное значение:", minimum)
print("Максимальное значение:", maximum)
print("Количество отрицательных чисел:", negative_count)
'''
#---------------------------------------------------------------
'''
number = input("Введите многозначное число: ")
sum_digits = sum(int(digit) for digit in number if digit.isdigit())
print("Сумма цифр числа:", sum_digits)
'''
#---------------------------------------------------------------