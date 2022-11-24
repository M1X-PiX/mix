import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Git и желтые окружности')
        self.btn = QPushButton('Draw', self)
        self.btn.move(170, 350)
        self.btn.resize(60, 40)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_crug(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_crug(self, qp):
        a = random.randint(10, 100)
        r = 255
        g = 255
        b = 0
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(random.randint(0, 200), random.randint(0, 200), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())