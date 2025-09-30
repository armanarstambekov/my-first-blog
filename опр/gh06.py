#Задание_1
'''
passworld = input("Ведите пароль: ")
if passworld == ("121212"):
    print("Пароль мовпал")
else:
    print("Пароль не совпал")
'''

'''
import re
def check_password(password):
    # Условия
    min_length = 8
    if len(password) < min_length:
        return "Пароль слишком короткий. Минимум 8 символов."
    if not re.search(r"[A-Z]", password):
        return "Пароль должен содержать хотя бы одну заглавную букву."
    if not re.search(r"[a-z]", password):
        return "Пароль должен содержать хотя бы одну строчную букву."
    if not re.search(r"\d", password):
        return "Пароль должен содержать хотя бы одну цифру."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Пароль должен содержать хотя бы один спецсимвол."
    return "Пароль надёжный!"
user_password = input("Введите пароль: ")
print(check_password(user_password))
'''

# Задание_2
'''
number = int(input("Введите число: "))
print(f"\n  {number}:\n")
for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")
'''
#Задание_3
'''
while True:
    try:
        n = int(input("Введите число (или 0 для выхода): "))
        if n == 0:
            print("Программа завершена.")
            break
        if n < 0:
            print("Введите положительное число.")
            continue
        total = sum(range(1, n))
        print(f"Сумма всех чисел до {n} (не включая его): {total}")
    except ValueError:
        print("Ошибка: введите целое число.")
'''


#Задание_4
import random
secret_number = random.randint(1, 100)
print("Я ЗАГОДАЛ ЧИСЛО")
attempts = 0
while True:
    try:
        guess = int(input("БРАТИК ТВОЯ ОЧЕРЕДЬ: "))
        attempts += 1
        if guess < secret_number:
            print("ЧИСЛО БОЛЬШЕ.")
        elif guess > secret_number:
            print("ЧИСЛО МЕНЬШЕ.")
        else:
            print(f"Я ВЫЙГРАЛ {secret_number} ЭТОТ {attempts} ТУРНИР.")
            break
    except ValueError:
        print("БРАТИК ИЛИ МАЛАЯ ВЫ ОШИБЛИСЬ ЕСЛИ ЧЁ.")


#Задание_5 НУЖНО ПРОВЕРИТЬ ПОЛЕНДРОПАМ


