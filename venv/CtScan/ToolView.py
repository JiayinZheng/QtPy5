import sys

import pymysql
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtGui import *

from MainWin3 import Ui_MainWindow


class ToolView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.images = ['./images/1.jpg', './images/2.jpg', './images/3.jpg', './images/4.jpg', './images/5.jpg',
                       './images/6.jpg', './images/7.jpg', './images/8.jpg', './images/9.jpg', './images/10.jpg',
                       './images/11.jpg', './images/12.jpg', './images/13.jpg']
        self.flag = False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUi()
        self.label_xy = []
        self.isMarked = False
    # def condb(self):
    #     db = pymysql.connect(host='localhost', port=3306, user='root', passwd='991128Lu', db='ct', charset='utf8')
    #     # configure and connect
    #     cursor = db.cursor()
    #     return db,cursor
    def initUi(self):
        # set label
        self.ui.comboBox.addItems(['Label 1', 'Label 2', 'Label 3', 'Label 4'])
        self.ui.comboBox.currentIndexChanged.connect(self.selectionChanged)

        # set opacity
        self.ui.opacity_slider.setMaximum(100)
        self.ui.opacity_slider.setMinimum(1)
        self.ui.opacity_slider.setValue(50)
        self.ui.opacity.setText(str(self.ui.opacity_slider.value()))
        self.ui.opacity_slider.valueChanged.connect(self.opacitySliderValueChanged)

        # set btn
        self.ui.magnifier.setText("")
        self.ui.magnifier.setIcon(QIcon("./images/magnifier.jpg"))
        self.ui.magnifier.resize(35, 39)
        self.ui.cursor_loc.setText("")
        self.ui.cursor_loc.setIcon(QIcon("./images/mouse.jpg"))
        self.ui.cursor_loc.resize(35, 39)
        self.ui.rectangle.setText("")
        self.ui.rectangle.setIcon(QIcon("./images/reg.png"))
        self.ui.rectangle.resize(35, 39)
        self.ui.pen.setText("")
        self.ui.pen.setIcon(QIcon("./images/pen.jpg"))
        self.ui.pen.resize(35, 39)
        print(self.ui.pen.sizeHint().height())
        print(self.ui.pen.sizeHint().width())
        self.ui.eraser.setText("")
        self.ui.eraser.setIcon(QIcon("./images/eraser.jpg"))
        self.ui.eraser.resize(35, 39)
        self.ui.undo.setText("")
        self.ui.undo.setIcon(QIcon("./images/redo.png"))
        self.ui.undo.resize(35, 39)
        self.ui.undo_all.setText("")
        self.ui.undo_all.setIcon(QIcon("./images/redoa.png"))
        self.ui.undo_all.resize(35, 39)
        self.ui.redo.setText("")
        self.ui.redo.setIcon(QIcon("./images/undo.png"))
        self.ui.redo.resize(35, 39)
        self.ui.btn_ok.setText("")
        self.ui.btn_ok.setIcon(QIcon("./images/ok.png"))
        self.ui.btn_ok.resize(35, 39)
        self.ui.btn_cancel.setText("")
        self.ui.btn_cancel.setIcon(QIcon("./images/cancel.png"))
        self.ui.btn_cancel.resize(35, 39)

        # 允许鼠标追踪
        self.ui.cursor_x.setMouseTracking(True)
        self.ui.cursor_y.setMouseTracking(True)

        # 设置照片
        self.ui.verticalSlider.setMaximum(12)
        self.ui.verticalSlider.setMinimum(0)
        self.ui.verticalSlider.setValue(0)
        self.ui.ct_view.setPixmap(QPixmap(self.images[self.ui.verticalSlider.value()]))
        self.ui.ct_view.setScaledContents(True)
        self.ui.verticalSlider.valueChanged.connect(self.viewSliderValueChanged)

        # 设置绘图方式
        self.ui.pen.clicked.connect(self.setPaintPen)
        self.ui.rectangle.clicked.connect(self.setPaintRect)

        # #点击确认响应函数
        self.ui.btn_ok.clicked.connect(self.okPressEvent)

    def okPressEvent(self):
        for i in self.ui.ct_view.label_xy:
            print(i)
    def selectionChanged(self, i):
        self.ui.ct_view.setText(self.ui.comboBox.currentText())
        print('current index', i, 'selection changed', self.ui.comboBox.currentText())

    def opacitySliderValueChanged(self):
        print('current opacity', self.ui.opacity_slider.value())
        self.ui.opacity.setText(str(self.ui.opacity_slider.value()))

    def viewSliderValueChanged(self):
        print('current photo path', self.images[self.ui.verticalSlider.value()])
        self.ui.ct_view.setPixmap(QPixmap(self.images[self.ui.verticalSlider.value()]))
        self.ui.ct_view.setScaledContents(True)

    def mouseMoveEvent(self, event):
        s = event.windowPos()
        self.ui.cursor_x.setMouseTracking(True)
        self.ui.cursor_y.setMouseTracking(True)
        self.ui.cursor_x.setText(str(s.x()))
        self.ui.cursor_y.setText(str(s.y()))
        self.ui.cursor_z.setText(str(self.ui.verticalSlider.value()))
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()

        self.update()

    # 鼠标点击事件
    def mousePressEvent(self, event):
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()
        self.update()

    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        self.flag = False
        self.update()

    def setPaintPen(self):
        self.ui.ct_view.paintStyle = "pen"
        self.ui.ct_view.isMarked = True

    def setPaintRect(self):
        self.ui.ct_view.paintStyle = "rect"




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/dog.jpg"))
    win = ToolView()
    win.show()
    sys.exit(app.exec_())
