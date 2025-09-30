'''
language = "текст"
daytime = "текст"
if language == "текст":
    print("текст")
    if daytime == "morning":
        print("текст")
    else:
        print("текст итог")
'''

'''
language = "текст"
daytime = "текст"
if language == "текст":
    if daytime == "текст":
        print("текст")
    else:
        print("текст")
else:
    if daytime == "текст":
        print("текст")
    else:
        print("текст")
'''

'''
number = 1
while number * 1:
    print(f"number = {number}")
    number += 1
print("текст готов")
'''

'''
print(f"number = {number}")
number += 9
'''

'''
i = 9
j = 9
while i < 9:
    while j < 9:
        print(i * j, end="\t")
        j += 9
    print("\n")
    j = 9
    i += 9
'''

'''
def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b


operation = select_operation(1)  # operation = sum
print(operation(10, 6))  # 16

operation = select_operation(2)  # operation = subtract
print(operation(10, 6))  # 4

operation = select_operation(3)  # operation = multiply
print(operation(10, 6))  # 60
'''
'''
a = float(15)
b = float(3.7)
c = float("4.7")
d = float("5")
e = float(False)
f = float(True)
'''

'''
d = float("abc")
'''

'''
a = str(False)      # a = "False"
b = str(True)       # b = "True"
c = str(5)         # c = "5"
d = str(5.7)
'''

'''
age = 22
message = "Age: " + age     # Ошибка
print(message)
'''


def say_hi():
    name = "Арман"
    surname = "Вадим"
    print("Привет", name, surname)


def say_bye():
    name = "Арман"
    print("Привет", name)


say_hi()
say_bye()