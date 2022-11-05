# from modules.lists import list_input
# from modules.number_functions import stop_input
stop_input = False
# 
list_input = []

def get_symbols(set_symbol):
    global stop_input
    list_input.append(set_symbol)
    stop_input = True
    print(stop_input)

def add_plus():
    get_symbols("+")

def add_minus():
    get_symbols("-")

def add_multiply():
    get_symbols("*")

def add_division():
    get_symbols("/")