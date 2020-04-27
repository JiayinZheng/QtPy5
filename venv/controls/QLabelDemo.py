import sys
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QApplication, QLabel, QWidget, QLineEdit, QPushButton
from PyQt5.QtGui import QPalette, QPixmap, QGradient
from PyQt5.QtCore import Qt


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Label Demo
        # label1 = QLabel(self)
        # label2 = QLabel(self)
        # label3 = QLabel(self)
        # label4 = QLabel(self)
        #
        # label1.setText("<font color=yellow>这是一个文本标签.</font>")
        # label1.setAutoFillBackground(True)
        # palette = QPalette()
        # palette.setColor(QPalette.Window, Qt.blue)
        # label1.setPalette(palette)
        # label1.setAlignment(Qt.AlignCenter)
        #
        # label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")
        #
        # label3.setAlignment(Qt.AlignCenter)
        # label3.setToolTip('这是一个图片标签')
        # label3.setPixmap(QPixmap('./images/dog.jpg'))
        #
        # label4.setOpenExternalLinks(True)
        # label4.setText("<a href='https://item.jd.com/12317265.html'>感谢关注</a>")
        #
        # vbox = QVBoxLayout()
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        #
        # label4.linkActivated.connect(self.linkClicked)
        # label2.linkHovered.connect(self.linkHovered)
        #
        # self.setLayout(vbox)
        # self.setWindowTitle("QLabel 控件演示")

        # Label setBuddy
        nameLabel = QLabel('&Name', self)
        nameLineEdit = QLineEdit(self)
        nameLabel.setBuddy(nameLineEdit)
        passwordLabel = QLabel('&Password', self)
        passwordLineEdit = QLineEdit(self)
        passwordLabel.setBuddy(passwordLineEdit)
        btnOk = QPushButton('确认')
        btnCancel = QPushButton('取消')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel, 0, 0)
        # 控件对象，rowIndex，columnIndex，占用行数，占用列数
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)
        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordLineEdit, 1, 1, 1, 2)
        mainLayout.addWidget(btnOk, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 3)

    def linkClicked(self):
        print('当鼠标点击label4标签时，触发事件')

    def linkHovered(self):
        print('当鼠标滑过Label2标签时，触发事件')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())