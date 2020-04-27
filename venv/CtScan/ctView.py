import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtGui import *
import nibabel as nb
from nibabel.viewers import OrthoSlicer3D
from nibabel import nifti1
import matplotlib

class ctView(QLabel):

    def __init__(self, layoutWidget):
        super().__init__()
        self.setMouseTracking(False)
        '''
         要想将按住鼠标后移动的轨迹保留在窗体上
         需要一个列表来保存所有移动过的点
        '''
        self.pos_xy = []
        self.label_xy = []
        self.isMarked = False
        self.paintStyle = ""
        self.x0 = 0
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0
        self.flag = False

    # 鼠标点击事件
    def mousePressEvent(self, event):
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()

    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        self.flag = False

    # 绘图
    # 鼠标点击事件
    def mouseMoveEvent(self, event):
        if self.paintStyle:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()

        """
         按住鼠标移动事件:将当前点添加到pos_xy列表中
         调用update()函数在这里相当于调用paintEvent()函数
         每次update()时，之前调用的paintEvent()留下的痕迹都会清空
        """
        # 中间变量pos_tmp提取当前点
        pos_tmp = (event.pos().x(), event.pos().y())
        # pos_tmp添加到self.pos_xy中
        self.pos_xy.append(pos_tmp)
        if self.isMarked:
            self.label_xy.append(pos_tmp)
        self.update()

    # 绘制事件
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.begin(self)
        if self.paintStyle == "rect":
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            rect = QRect(self.x0, self.y0, abs(self.x1 - self.x0), abs(self.y1 - self.y0))
            painter.drawRect(rect)
        if self.paintStyle == "pen":
            '''
                 首先判断pos_xy列表中是不是至少有两个点了
                 然后将pos_xy中第一个点赋值给point_start
                 利用中间变量pos_tmp遍历整个pos_xy列表
                  point_end = pos_tmp
                  画point_start到point_end之间的线
                  point_start = point_end
                 这样，不断地将相邻两个点之间画线，就能留下鼠标移动轨迹了
                '''
            if len(self.pos_xy) > 1:
                point_start = self.pos_xy[0]
                for pos_tmp in self.pos_xy:
                    point_end = pos_tmp
                    painter.drawLine(point_start[0], point_start[1], point_end[0], point_end[1])
                    point_start = point_end
        painter.end()

    def okPressEvent(self):
        pass
