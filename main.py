from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5 import uic
from random import randint
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setFixedSize(600, 500)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
            print("end")

    def paint(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def draw_flag(self, qp):
        try:
            qp.setBrush(QColor('yellow'))
            w = randint(10, 400)
            qp.drawEllipse(480 - w, 400 - w, w, w)
        except Exception:
            print("1")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
