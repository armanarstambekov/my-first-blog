#Задание_1
'''
a = float(input("ведите первое число: "))
b = float(input("ведите второе число: "))
if a > b:
    print("первое число больше")
elif a == b:
    print("воторе число равны")
else:
    print("воторе число больше")
'''
#Задание_2
'''
name = input("ведите ваше имя: ")
surname = input("ведите ваше фамилию: ")
print("вас зовут", name, surname)
'''

#Задание_3
'''
for n in range(1, 21):
    input("ведите фамилию: ")
'''

#Задание_4
'''
number = 7
while number < 15:
    number+=1
    print(number)
'''
#Задание_4
'''
for n in range(0, 51, 2):
    print(n, end=" ")
'''
#Задание_5
'''
a = int(input("веди первое число: "))
b = int(input("веди второе число: "))
while a < b:
    a += 1
    print(a)
'''

# Задание_6
'''
def input_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")
start = input_number("Введите первое число: ")
end = input_number("Введите второе число: ")
if start > end:
    start, end = end, start
print(f"Чётные числа от {start} до {end}:")
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end=' ')
'''

'''
a = int(input("веди первое число: "))
b = int(input("веди второе число: "))
while a < b:
    a += 1
    if a % 2 == 0:
        print(a, end=" ")
'''
'''
a = int(input("веди первое число: "))
b = int(input("веди второе число: "))
while a < b:
    a += 1
    if a % 2 == 0:
        print("четное число: ", a)
    else:
        print("не четное число: ", a)
'''