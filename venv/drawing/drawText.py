import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QRect


class DrawText(QWidget):
    def __init__(self):
        super(DrawText, self).__init__()
        self.setWindowTitle('在窗口上绘制各种图形')
        self.resize(300, 200)
        self.text = "Python 从菜鸟到高手"

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)

        # 绘制弧
        rect = QRect(0, 10, 100, 100)
        painter.drawArc(rect, 0, 50*16)

        # 通过弧绘制圆
        painter.setPen(Qt.red)
        painter.drawArc(120, 10, 100, 100, 0, 360*16)

        # 绘制带弦的弧

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DrawText()
    win.show()
    sys.exit(app.exec_())
