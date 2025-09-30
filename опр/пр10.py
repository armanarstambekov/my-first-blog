#-------------------------------------------------------------------------------
#повторение "Классы и объекты"
'''
class Person:
    def __init__(self, name, age, phone, brand, yer):
        self.name = name
        self.age = age
        self.phone = phone
        self.brand = brand
        self.yer = yer
    def get_info(self):
        return f"Имя: {self.name}\nВозраст: {self.age}\nТелефон: {self.phone} \nБренд: {self.brand} \nГод: {self.yer}"
person1 = Person("Вика", 18, "+77473698521")
person2 = Person("Арман", 22, "+77473488986")
person3 = Person("ipone 12")
person4 = Person("apple")
print("Информация о первом человеке:")
print(person1.get_info())
print("\nИнформация о втором человеке:")
print(person2.get_info())
print("Информация о телефоне:")
print(person3.get_info())
print("Информация о бренд:")
print(person4.get_info())
'''
import os.path
from fileinput import filename

from message import hello

#-------------------------------------------------------------------------------
#1.1 - Модули
#1.2 - Определение и подключение модулей
#-------------------------------------------------------------------------------
'''
import message
print(message.hello)
message.print_message("Bro hello")
'''
#-------------------------------------------------------------------------------
'''
from message import print_message
print_message("Hello work")
'''
#-------------------------------------------------------------------------------
'''
from message import *
print_message("hello work")
print(hello)
'''
#-------------------------------------------------------------------------------
'''
from message import *
print_message("hello work")
def print_message(some_text):
    print(f"text: {some_text}")
print_message("hello work")
'''
#-------------------------------------------------------------------------------
'''
import message as mes
print(mes.hello)
mes.print_message("hello work")
'''
#-------------------------------------------------------------------------------
'''
from message import print_message as display
from message import hello as welcome
print(welcome)
display("hello work")
'''
#-------------------------------------------------------------------------------
'''
myfile = open("hello.txt", "w")
#myfile.close()
import os
def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words
def get_words_dict(words):
    words_dict = dict()
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict
def main():
    filename = input("Введите путь к файлу: ")
    if not os.path.exists(filename):
        print("Указанный файл не существует")
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        print(f"Кол-во слов: {len(words)}")
        print(f"Кол-во уникальных слов: {len(words_dict)}")
        print("Все использованные слова:")
        for word in words_dict:
            print(word.ljust(20), words_dict[word])
if __name__ == "__main__":
    main()
    import os
    def get_words(filename):
        with open(filename, encoding="utf8") as file:
            text = file.read()
        text = text.replace("\n", " ")
        text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
        text = text.lower()
        words = text.split()
        words.sort()
        return words
    def get_words_dict(words):
        words_dict = dict()
        for word in words:
            if word in words_dict:
                words_dict[word] = words_dict[word] + 1
            else:
                words_dict[word] = 1
        return words_dict
    def main():
        filename = input("Введите путь к файлу: ")
        if not os.path.exists(filename):
            print("Указанный файл не существует")
        else:
            words = get_words(filename)
            words_dict = get_words_dict(words)
            print(f"Кол-во слов: {len(words)}")
            print(f"Кол-во уникальных слов: {len(words_dict)}")
            print("Все использованные слова:")
            for word in words_dict:
                print(word.ljust(20), words_dict[word])
    if __name__ == "__main__":
        main()
'''
#-------------------------------------------------------------------------------
