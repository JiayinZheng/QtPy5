# 居中程序，添加按钮以及事件
import sys

from PyQt5.QtWidgets import QDesktopWidget, QPushButton, QMainWindow, QApplication, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):
    def __init__(self, parent=None):
        super(CenterForm, self).__init__(parent)

        # 设置主窗口标题
        self.setWindowTitle("First MainWindow")

        # 设置窗口尺寸
        self.resize(400, 300)

        # 添加Button
        self.button1 = QPushButton('退出应用程序')
        self.button1.clicked.connect(self.onClick_Button)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft, newTop)

    # 按钮单击事件的方法（自定义的槽）
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + '按钮被按下')
        app = QApplication.instance()
        # 退出应用程序
        app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = CenterForm()
    main.show()

    sys.exit(app.exec_())