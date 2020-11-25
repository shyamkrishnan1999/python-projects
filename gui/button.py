from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

def window():

    app = QApplication([])
    win=QMainWindow()
    win.setGeometry(500,500,300,300)
    win.setWindowTitle("Hey!")

    label = QLabel(win)

    def clicked():
        label.setText("Wtsapp")
        label.setAlignment(Qt.AlignCenter)
        label.move(100,0)

    button = QPushButton("Click me",win)
    button.resize(100,50)
    button.move(100,100)
    button.clicked.connect(clicked)

    win.show()
    app.exec()




window()

