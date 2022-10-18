import time
from modules.windows import *
from modules.lists import *
from modules.layouts import *
from modules.buttons import *

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

#
add_buttons()
#
addToLayout()
#
win.setLayout(main_V)    
#
win.show()
#
app.exec_()



