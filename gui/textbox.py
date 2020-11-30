from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class mywindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title="Myapp"
        self.width=300
        self.height=300
        self.left=100
        self.top=100
        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.button=QPushButton(self)
        self.button.move(100,150)
        self.button.setText("Click")

        self.textbox=QLineEdit(self)
        self.textbox.move(100,100)

        self.label=QLabel(self)
        self.label.move(100,200)

        self.button.clicked.connect(self.onclick)
        self.show()

    @pyqtSlot()

    def onclick(self):

        textboxvalue=self.textbox.text()
        self.label.setText("Hello "+textboxvalue)


app=QApplication([])
window=mywindow()
app.exec()




