from modules.labels import label
from modules.fonts import font1
# from modules.lists import list_input
from modules.symbol_functions import stop_input
#
number = ""
# stop_input = False

def get_number(symbol_number):
    global number
    #
    if len(number) != 16:
        print(stop_input)
        if stop_input:
            list_input.append(number)
            number = ""
        if not stop_input:
            number += str(symbol_number) #
        label.setText(number) #

def add_zero():
    get_number(0)

def add_one():
    get_number(1)

def add_two():
    get_number(2)

def add_three():
    get_number(3)

def add_four():
    get_number(4)

def add_five():
    get_number(5)

def add_six():
    get_number(6)

def add_seven():
    get_number(7)

def add_eight():
    get_number(8)

def add_nine():
    get_number(9)





