import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.flag = False
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Рисование')
        self.setMouseTracking(True)
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.draw(3)

    def mouseMoveEvent(self, event):
        self.a, self.b = event.x(), event.y()

    def mousePressEvent(self, event):
        self.a, self.b = event.x(), event.y()
        if event.button() == Qt.LeftButton:
            self.draw(1)
        elif (event.button() == Qt.RightButton):
            self.draw(2)

    def draw(self, num):
        self.flag = num
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawFlag(qp)
            qp.end()

    def drawFlag(self, qp):
        if self.flag == 1:
            qp.drawRect(self.a, self.b, 20, 20)
        elif self.flag == 2:
            qp.drawEllipse(self.a, self.b, 20, 20)
        elif self.flag == 3:
            qp.drawLine(self.a, self.b, self.a + 20, self.b + 20)
            qp.drawLine(self.a, self.b, self.a - 20, self.b + 20)
            qp.drawLine(self.a + 20, self.b + 20, self.a - 20, self.b + 20)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())