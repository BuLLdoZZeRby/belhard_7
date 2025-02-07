"""
С помощью декораторов реализовать конвейер сборки бургера

Написать декоратор bread, который:
 - до декорируемой функции будет печатать "</------------\\>"
 - после декорируемой функции будет печатать "<\\____________/>"


Написать декоратор tomato, который:
 - до декорируемой функции будет печатать "*** помидоры ****"

Написать декоратор salad, который:
 - до декорируемой функции будет печатать "~~~~ салат ~~~~~"

Написать декоратор cheese, который:
 - до декорируемой функции будет печатать "^^^^^ сыр ^^^^^^"

Написать декоратор onion, который:
 - до декорируемой функции будет печатать "----- лук ------"

Написать функцию beef, которая:
 - печатает "### говядина ###"

Написать функцию chicken, которая:
 - печатает "|||| курица ||||"

1) Собрать с помощью декораторов гамбургер:
    - булка
    - лук
    - помидоры
    - говядина
    - булка

2) Собрать с помощью декораторов чикенбургер:
    - булка
    - сыр
    - салат
    - курица
    - булка
"""


def bread(func):
    def wrepper():
        print("</------------\\>")
        func()
        print("<\\____________/>")
    return wrepper


def tomato(func):
    def wrepper():
        print("*** помидоры ****")
        func()
    return wrepper


def salad(func):
    def wrepper():
        print("~~~~ салат ~~~~~")
        func()
    return wrepper


def cheese(func):
    def wrepper():
        print("^^^^^ сыр ^^^^^^")
        func()
    return wrepper


def onion(func):
    def wrepper():
        print("----- лук ------")
        func()
    return wrepper


@bread
@onion
@tomato
def beef():
    print("### говядина ###")


@bread
@cheese
@salad
def chicken():
    print("|||| курица ||||")
