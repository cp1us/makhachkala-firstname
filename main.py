import sys
from random import randint
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor


class LinusIsGit(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.figures = []
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diam = randint(5, 300)
        x, y = randint(0, self.width() - diam), randint(0, self.height() - diam)
        self.figures.append((x, y, diam))
        print('linus')
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for x, y, diam in self.figures:
            painter.setBrush(QColor("green"))
            painter.drawEllipse(x, y, diam, diam)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = LinusIsGit()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())