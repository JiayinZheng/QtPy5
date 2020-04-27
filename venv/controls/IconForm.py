import sys

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class IconForm(QMainWindow):
    def __init__(self, parent=None):
        super(IconForm, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle("设置窗口图标") # 只在Windows系统下可用，但QApplication的setWindowIcon是调用了这个方法，但在非Windows系统下可用
        self.setWindowIcon(QIcon('./images/dog.jpg'))

        self.button1 = QPushButton('我是一个按钮')
        self.button1.setToolTip("你好呀，快点击")

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/dog.jpg"))
    main = IconForm()
    main.show()

    sys.exit(app.exec_())