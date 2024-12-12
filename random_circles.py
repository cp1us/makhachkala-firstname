import sys
import random
from PyQt6 import QtCore, QtGui, QtWidgets


class LinusIsSoGit(QtWidgets.QMainWindow):

    COLOURS = ('black', 'red', 'green', 'blue', 'white', 'yellow', 'orange', 'purple')

    def __init__(self):
        super().__init__()
        self.initUi()
        self.retranslateUi()
        self.figures = []
        self.pushButton.clicked.connect(self.draw_circle)

    def initUi(self):
        self.setObjectName("MainWindow")
        self.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 20, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "круг"))
        self.pushButton.setText(_translate("MainWindow", "Circle!"))

    def draw_circle(self):
        diam = random.randint(5, 300)
        x, y = random.randint(0, self.width() - diam), random.randint(0, self.height() - diam)
        color = random.choice(self.COLOURS)
        self.figures.append((x, y, diam, color))
        print('linus')
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        for x, y, diam, color in self.figures:
            painter.setBrush(QtGui.QColor(color))
            painter.drawEllipse(x, y, diam, diam)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = LinusIsSoGit()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
