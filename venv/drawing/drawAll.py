import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class DrawAll(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('在窗口上绘制文本')
        self.resize(300, 200)
        self.text = "Python 从菜鸟到高手"

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        print("aaa")
        painter.setPen(QColor(150, 43, 5))
        painter.setFont(QFont('SimSun', 25))

        painter.drawText(event.rect(), Qt.AlignCenter, self.text)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DrawAll()
    win.show()
    sys.exit(app.exec_())
