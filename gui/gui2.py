from PyQt5.QtWidgets import QApplication,QWidget

def widget():
    app=QApplication([])
    wid=QWidget()
    wid.show()
    app.exec_()

widget()