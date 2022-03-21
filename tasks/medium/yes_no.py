"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(number):
    list_number = []
    for i in number:
        if i not in list_number:
            list_number.append(i)
            print("No")
        else:
            print("Yes")
