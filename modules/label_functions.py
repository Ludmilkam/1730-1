from modules.labels import label
from modules.fonts import font1
#
number = ""
#
def get_symbols(symbol):
    global number
    #
    if len(number) != 16:
        number += str(symbol) #
        label.setText(number) #
#
def add_zero():
    get_symbols(1)






