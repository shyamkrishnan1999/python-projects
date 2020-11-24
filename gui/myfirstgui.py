from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtCore import Qt

def window():
    #Declares app
    app=QApplication([])

    #Setting properties of the Window.
    win=QMainWindow()
    win.setWindowTitle("GUI")
    win.setGeometry(500,300,250,300)

    #Declaring a label and aligning it.
    label=QLabel("Hello")
    label.setAlignment(Qt.AlignCenter)

    #Setting the label in the window
    win.setCentralWidget(label)
    win.show()

    #Starts app
    app.exec_()

window()

