import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
#        self.setFixedSize(600, 1000)
        self.setGeometry(50, 50, 600, 1000)
        self.setWindowTitle("Festival Controller")
        self.setWindowIcon(QtGui.QIcon('inhun_favicon.png'))
        self.home()

    def home(self):
        snackbar_btn = QtGui.QPushButton("")

        quit_btn = QtGui.QPushButton("", self)
        quit_btn.clicked.connect(self.home2)
#        quit_btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        quit_btn.setIcon(QtGui.QIcon('inhun_favicon.png'))
        quit_btn.setIconSize(QtCore.QSize(100, 100))
        quit_btn.resize(100, 100)
        quit_btn.move(100, 100)
        self.show()
    
    def home2(self):
        self.close()
        print("home2")
        btn1 = QtGui.QPushButton("snack Image", self)
        btn1.resize(300, 300)
        btn1.move(200, 200)

        btn2 = QtGui.QPushButton("Buy", self)
        btn2.resize(100, 100)
        btn2.move(250, 400)
        self.show()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
