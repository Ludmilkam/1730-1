from PyQt5.QtWidgets import (
        QWidget, 
        QApplication
    )

app = QApplication([])
#
win = QWidget()
#
win.resize(300, 400)
#
win.setWindowTitle("Calculator")