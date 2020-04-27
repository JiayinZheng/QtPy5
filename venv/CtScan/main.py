import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import MainWin2
import login

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("./images/dog.jpg"))
    # MainWindow = QMainWindow()
    # ui = MainWin2.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/dog.jpg"))
    MainWindow = QMainWindow()
    ui = login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
