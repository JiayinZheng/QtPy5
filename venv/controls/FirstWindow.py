import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class FirstMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWindow, self).__init__(parent)

        # 设置主窗口标题
        self.setWindowTitle("First MainWindow")

        # 设置窗口尺寸
        self.resize(400, 300)

        self.status = self.statusBar()

        self.status.showMessage('只存在5秒的消息', 5000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/dog.jpg"))
    main = FirstMainWindow()
    main.show()

    sys.exit(app.exec_())