import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QPixmap, QGradient
from PyQt5.QtCore import Qt

# QLineEdit空间和回显模式
# 基本功能:输入单行文本
# EchoMode(回显模式)
#
# 1 Normal
# 2 NoEcho
# 3 Password
# 4 PasswordEchoEdit


class QLineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')
        formLayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow("Normal", normalLineEdit)
        formLayout.addRow("NoEcho", noEchoLineEdit)
        formLayout.addRow("Password", passwordLineEdit)
        formLayout.addRow("PasswordEchoOnEdit", passwordEchoOnEditLineEdit)

        normalLineEdit.setPlaceholderText("normal")
        noEchoLineEdit.setPlaceholderText("noEcho")
        passwordLineEdit.setPlaceholderText("password")
        passwordEchoOnEditLineEdit.setPlaceholderText("passwordEcho")

        # 回显模式
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QLineEditDemo()
    main.show()
    sys.exit(app.exec_())