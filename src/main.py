"""
pyqt5 App for pm4py

author: boer
last edited: 2022-12-29
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QMenu, QFileDialog, QMessageBox, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QPainter, QImage
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
# QPattern
from shutil import copy
import os
import cv2 as cv
from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_contrast_ratio import Ui_Form
from ui.ui_smooth_sharp import Ui_Form_sp
from ui.ui_Fourier import Ui_Form_f
from img_pro_utils import *
from ui.ui_noise import Ui_Form_noise
from ui.ui_edge import Ui_Form_edge
from ui.ui_binary import Ui_Form_bin


# 工具类

class Utils:
    @staticmethod
    def get_all_files_in_dir(dir_path):
        return [os.path.join(dir_path, i) for i in os.listdir(dir_path)]

    @staticmethod
    def get_all_files_in_dir_by_type(dir_path, file_type):
        return [os.path.join(dir_path, i) for i in os.listdir(dir_path) if i.endswith(file_type)]

    @staticmethod
    def get_all_filenames_in_dir(dir_path):
        return [i for i in os.listdir(dir_path)]


class MainWindow(QMainWindow, Ui_MainWindow):

    switch_contrast_ratio_window = QtCore.pyqtSignal()  # 跳转信号，在主页面跳转到对比度页面
    switch_smooth_sharp_window = QtCore.pyqtSignal()  # 跳转信号，在主页面跳转到平滑锐化页面
    switch_fourier_window = QtCore.pyqtSignal()  # 跳转信号，在主页面跳转到傅里叶变换页面
    switch_noise_window = QtCore.pyqtSignal()  # 跳转信号，在主页面跳转到页面
    switch_edge_window = QtCore.pyqtSignal()  # 跳转信号，在主页面跳转到边缘检测页面
    switch_bin_window = QtCore.pyqtSignal()  # 跳转信号，在主页面跳转到二值化页面

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.img_origin = None
        self.img = None
        self.img_origin_pixmap = None
        self.img_qimage = None

        # 设置滚动条
        self.graphicsView.horizontalScrollBar().setTracking(False)
        self.graphicsView.verticalScrollBar().setTracking(False)
        self.graphicsView.setInteractive(True)
        self.graphicsView.setMouseTracking(True)

        # 设置滚动条_2
        self.graphicsView_2.horizontalScrollBar().setTracking(False)
        self.graphicsView_2.verticalScrollBar().setTracking(False)
        self.graphicsView_2.setInteractive(True)
        self.graphicsView_2.setMouseTracking(True)

        self.actionimport_img.triggered.connect(self.import_img)
        self.actionexport_as_png.triggered.connect(self.export_as_png)
        self.actionopen_data_dir.triggered.connect(self.open_dir)
        self.actionsave.triggered.connect(self.save)
        self.comboBox.addItems(Utils.get_all_filenames_in_dir("./data"))
        self.change_img()  # 初始化图片
        self.comboBox.currentIndexChanged.connect(self.change_img)
        self.pushButton.clicked.connect(self.fresh_img)
        self.listWidget.itemClicked.connect(self.on_listWidget_item_clicked)
        self.listWidget_2.itemClicked.connect(self.on_listWidget2_item_clicked)
        self.listWidget_3.itemClicked.connect(self.on_listWidget3_item_clicked)
        self.listWidget_4.itemClicked.connect(self.on_listWidget4_item_clicked)

    def save(self):
        pathName = "./data/" + self.comboBox.currentText()
        cv.imwrite(pathName, self.img)
        self.statusBar().showMessage("保存成功,覆盖原图,保存路径为" + pathName,)
        self.change_img()

    def fresh_img(self):
        self.graphicsView.fitInView(QGraphicsPixmapItem(
            self.img_origin_pixmap).boundingRect(), Qt.KeepAspectRatio)
        self.graphicsView_2.fitInView(QGraphicsPixmapItem(
            self.img_origin_pixmap).boundingRect(), Qt.KeepAspectRatio)

    def change_img(self):
        pathName = "./data/" + self.comboBox.currentText()
        try:
            img = cv.imread(pathName)
            if len(img.shape) == 3:
                img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            self.img_origin = img
        except:
            self.statusBar().showMessage("导入图片失败")
            print("导入图片失败")
            return
        if self.img_origin is None:
            self.statusBar().showMessage("导入图片失败，图片路径中不能包含中文")
            return

        self.img = self.img_origin.copy()
        self.img_origin_pixmap = QPixmap(pathName)
        # 将self.img倒序，因为opencv读取的图片是BGR格式，而QImage是RGB格式
        # self.img_qimage = QImage(
        # self.img, self.img.shape[1], self.img.shape[0], self.img.shape[1] * 3, QImage.Format_RGB888)
        # 灰度图读入方法
        self.img_qimage = QImage(
            self.img, self.img.shape[1], self.img.shape[0], self.img.shape[1] * 1, QImage.Format_Grayscale8)
        # 显示原始图片
        pixmap = QPixmap.fromImage(self.img_qimage)
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.graphicsView.setScene(scene)

        self.show_image()

    def import_img(self):
        # 使用getOpenFileNames()方法获取多个文件的路径
        pathNames, fileType = QFileDialog.getOpenFileNames(
            self, "选取文件", "./", "PNG Files (*.png)")
        for i in pathNames:
            copy(i, "./data")
        self.comboBox.clear()
        self.comboBox.addItems(Utils.get_all_filenames_in_dir("./data"))

    def export_as_png(self):
        pathName, fileType = QFileDialog.getSaveFileName(
            self, "保存文件", "./", "PNG Files (*.png)")
        # copy()
        pathName, fileType
        cv.imwrite(pathName, self.img)


    # def pop_up_open_files_window(self):
    #     fileNames, fileType = QFileDialog.getOpenFileNames(
    #         self, "选取文件", "./", "All Files (*);;CSV Files (*.csv);;XES Fioles(*.xes)")

    #     for i in fileNames:
    #         copy(i, "./data")
    #     # 刷新下拉框

    def open_dir(self):
        os.popen("explorer.exe .\\data")
        # 更新图片选项
        self.comboBox.clear()
        self.comboBox.addItems(Utils.get_all_filenames_in_dir("./data"))

    def show_image(self):
        """第二张图片更新方法
        """
        print(self.img.shape[1])
        print(self.img.shape[0])
        print(self.img.shape[1] * 1)
        print(type(self.img))
        print(type(self.img[0][0]))
        self.img_qimage = QImage(
            self.img, self.img.shape[1], self.img.shape[0], self.img.shape[1] * 1, QImage.Format_Grayscale8)

        # 显示原始图片
        pixmap = QPixmap.fromImage(self.img_qimage)
        scene = QGraphicsScene()
        # 显示在GraphicsView中
        scene.addPixmap(pixmap)
        self.graphicsView_2.setScene(scene)
        # # 设置允许使用鼠标滚轮缩放
        # self.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        # self.graphicsView.setInteractive(True)
        # self.graphicsView.setMouseTracking(True)
        # self.graphicsView.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        # self.graphicsView.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        # self.graphicsView.setRenderHint(QPainter.Antialiasing)
        # self.graphicsView.setRenderHint(QPainter.SmoothPixmapTransform)
        # self.graphicsView.setRenderHint(QPainter.HighQualityAntialiasing)
        # self.graphicsView.setRenderHint(QPainter.TextAntialiasing)
        # self.graphicsView.setRenderHint(QPainter.LosslessImageRendering)
        # self.graphicsView.setRenderHint(QPainter.NonCosmeticDefaultPen)

        # # 启用缩放功能
        # self.graphicsView.setRenderHint(QPainter.SmoothPixmapTransform)
        # # 设置缩放锚点，即缩放中心，这里设置为鼠标所在位置
        # self.graphicsView.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        # # 设置缩放时的锚点，这里设置为鼠标所在位置
        # self.graphicsView.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        # # 设置滚轮缩放的步长
        # self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        # self.graphicsView.setOptimizationFlag(QGraphicsView.DontAdjustForAntialiasing, True)
        # self.graphicsView.setOptimizationFlag(QGraphicsView.DontSavePainterState, True)
        # self.graphicsView.setRenderHint(QPainter.Antialiasing)
        # self.graphicsView.setRenderHint(QPainter.TextAntialiasing)

    def wheelEvent(self, event):
        """graphicsView滚轮事件，缩放图片

        Args:
            event (_type_): _description_
        """
        # 如果鼠标滚轮向上滚动，放大图片
        if event.angleDelta().y() > 0:
            self.graphicsView.scale(1.1, 1.1)
            self.graphicsView_2.scale(1.1, 1.1)
        else:
            self.graphicsView.scale(0.9, 0.9)
            self.graphicsView_2.scale(0.9, 0.9)
    # def wheelEvent2(self, event):
    #     """graphicsView滚轮事件，缩放图片

    #     Args:
    #         event (_type_): _description_
    #     """
    #     if event.source() == self.graphicsView_2:
    #         # 如果鼠标滚轮向上滚动，放大图片
    #         if event.angleDelta().y() > 0:
    #             self.graphicsView_2.scale(1.1, 1.1)
    #         else:
    #             self.graphicsView_2.scale(0.9, 0.9)

    def on_listWidget_item_clicked(self):
        # 将其他所有item的状态设置为未选中
        self.listWidget_2.clearSelection()
        self.listWidget_3.clearSelection()
        self.listWidget_4.clearSelection()
        print(self.listWidget.currentItem().text())
        # self.img_qimage = Utils.get_qimage_from_path(item.text())
        txt = self.listWidget.currentItem().text()
        if txt == "对比度":
            # 线性变换
            # 发送信号打开页面ui_form
            self.switch_contrast_ratio_window.emit()
        elif txt == "平滑及锐化":
            self.switch_smooth_sharp_window.emit()
        elif txt == "图形学":
            print("图形学")
            pass
        elif txt == "加噪":
            self.switch_noise_window.emit()
        elif txt == "边缘提取":
            self.switch_edge_window.emit()
        self.show_image()

    def on_listWidget2_item_clicked(self):
        # 将其他所有item的状态设置为未选中
        self.listWidget.clearSelection()
        self.listWidget_3.clearSelection()
        self.listWidget_4.clearSelection()
        print(self.listWidget_2.currentItem().text())
        if self.listWidget_2.currentItem().text() == "滤波":
            self.switch_fourier_window.emit()
        self.show_image()

    def on_listWidget3_item_clicked(self):
        # 将其他所有item的状态设置为未选中
        self.listWidget.clearSelection()
        self.listWidget_2.clearSelection()
        self.listWidget_4.clearSelection()
        print(self.listWidget_3.currentItem().text())
        if self.listWidget_3.currentItem().text() == "图像二值化":
            self.switch_bin_window.emit()
        self.show_image()

    def on_listWidget4_item_clicked(self):
        # 将其他所有item的状态设置为未选中
        self.listWidget.clearSelection()
        self.listWidget_2.clearSelection()
        self.listWidget_3.clearSelection()
        print(self.listWidget_4.currentItem().text())
        if self.listWidget_4.currentItem().text() == "抠图(前景背景分离)":
            print("抠图")
            self.img = Img_pro_utils.segment(Img_pro_utils, self.img_origin)
        self.show_image()



class Contrast_ratio_window(QWidget, Ui_Form):
    img_origin = None
    img = None
    switch_execute_img_pro = QtCore.pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        # 设置只能允许数字输入
        self.le_b.setValidator(QtGui.QDoubleValidator())  # 设置只能输入double类型的数据
        self.le_k.setValidator(QtGui.QDoubleValidator())  # 设置只能输入double类型的数据
        self.le_lamb_log.setValidator(
            QtGui.QDoubleValidator())  # 设置只能输入double类型的数据
        self.le_base_log.setValidator(
            QtGui.QDoubleValidator())  # 设置只能输入double类型的数据
        self.le_lamb_power.setValidator(
            QtGui.QDoubleValidator())  # 设置只能输入double类型的数据
        self.le_power.setValidator(
            QtGui.QDoubleValidator())  # 设置只能输入double类型的数据
        self.pb_line.clicked.connect(self.imLineAdjust)
        self.pb_log.clicked.connect(self.imLogAdjust)
        self.pb_power.clicked.connect(self.imPowerAdjust)
        self.pb_hisEqual.clicked.connect(self.imHistEqual)

    def imLineAdjust(self):
        k = self.le_k.text()
        b = self.le_b.text()
        if (k == "" or b == ""):
            print("k or b is null")
            return
        k = float(k)
        b = float(b)
        self.img = Img_pro_utils.imLinearAdjust(
            Img_pro_utils, self.img_origin, k, b)
        self.switch_execute_img_pro.emit()  # 发送处理完成信号

    def imLogAdjust(self):
        lamb = self.le_lamb_log.text()
        base = self.le_base_log.text()
        lamb = float(lamb)
        base = float(base)
        self.img = Img_pro_utils.imLogAdjust(
            Img_pro_utils, self.img_origin, lamb, base)
        self.switch_execute_img_pro.emit()  # 发送处理完成信号

    def imPowerAdjust(self):
        lamb = self.le_lamb_power.text()
        power = self.le_power.text()
        lamb = float(lamb)
        power = float(power)
        self.img = Img_pro_utils.imPowerAdjust(
            Img_pro_utils, self.img_origin, lamb, power)
        print(self.img)
        self.switch_execute_img_pro.emit()  # 发送处理完成信号

    def imHistEqual(self):
        self.img = Img_pro_utils.imHistEqual(Img_pro_utils, self.img_origin)
        self.switch_execute_img_pro.emit()


class Smooth_sharp_window(QWidget, Ui_Form_sp):
    img_origin = None
    img = None
    switch_execute_img_pro = QtCore.pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.pb_smooth.clicked.connect(self.imSmooth)
        self.pb_sharp.clicked.connect(self.imSharp)

    def imSmooth(self):
        self.img = Img_pro_utils.imSmoothing(Img_pro_utils, self.img_origin)
        self.switch_execute_img_pro.emit()  # 发送处理完成信号

    def imSharp(self):
        self.img = Img_pro_utils.imSharpen(Img_pro_utils, self.img_origin)
        print(self.img)
        self.switch_execute_img_pro.emit()  # 发送处理完成信号


class Noise_window(QWidget, Ui_Form_noise):
    img_origin = None
    img = None
    switch_execute_img_pro = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_s.clicked.connect(self.sp_noise)
        self.pb_g.clicked.connect(self.gaussian_noise)
        self.pb_r.clicked.connect(self.random_noise)
        self.le_sn.setValidator(QtGui.QDoubleValidator())  # 设置只能输入double类型的数据
        self.le_sigma.setValidator(
            QtGui.QDoubleValidator())  # 设置只能输入double类型的数据

    def sp_noise(self):
        n = float(self.le_sn.text())
        self.img = Img_pro_utils.sp_noise(Img_pro_utils, self.img_origin, n)
        self.switch_execute_img_pro.emit()  # 发送处理完成信号

    def gaussian_noise(self):
        mean = int(self.le_mean.text())
        sigma = float(self.le_sigma.text())
        self.img = Img_pro_utils.gaussian_noise(Img_pro_utils, self.img_origin, mean, sigma)
        self.switch_execute_img_pro.emit()

    def random_noise(self):
        n = int(self.le_rn.text())
        sigma = float(self.le_sigma.text())
        self.img = Img_pro_utils.random_noise(Img_pro_utils, self.img_origin, n, sigma)
        self.switch_execute_img_pro.emit()
class Edge_window(QWidget, Ui_Form_edge):
    img_origin = None
    img = None
    switch_execute_img_pro = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.imEdge)
    
    def imEdge(self):
        type = self.comboBox.currentText()
        self.img = Img_pro_utils.imEdge(Img_pro_utils, self.img_origin, type)
        self.switch_execute_img_pro.emit()


class Binary_Window(QWidget, Ui_Form_bin):
    img_origin = None
    img = None
    switch_execute_img_pro = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.mo)
    
    def mo(self):
        type = self.comboBox.currentText()
        ksize = int(self.lineEdit.text())
        self.img = Img_pro_utils.morphology(Img_pro_utils, self.img_origin, type, ksize)
        self.switch_execute_img_pro.emit() 

class Fourier_window(QWidget, Ui_Form_f):
    img_origin = None
    img = None
    switch_execute_img_pro = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_Fimg.clicked.connect(self.imFimg)
        self.pb_filter.clicked.connect(self.filter)
        self.le_d0.setValidator(QtGui.QDoubleValidator())  # 设置只能输入double类型的数据
        self.le_n.setValidator(QtGui.QDoubleValidator())  # 设置只能输入double类型的数据

    def imFimg(self):
        self.img = Img_pro_utils.imFimg(Img_pro_utils, self.img_origin)
        print(self.img)
        self.switch_execute_img_pro.emit()  # 发送处理完成信号

    def filter(self):
        d0 = self.le_d0.text()
        d0 = float(d0)
        n = self.le_n.text()
        n = float(n)
        type = self.type.currentText()  # 高通或者低通
        kind = self.kind.currentText()  # 滤波器种类
        self.img = Img_pro_utils.filter(
            Img_pro_utils, self.img_origin, d0, n, type, kind)
        self.switch_execute_img_pro.emit()  # 发送处理完成信号


class Controller:

    """页面跳转控制器
    """
    img = None  # 用于传递图片的中间变量

    def __init__(self):
        pass

    def show_start_page(self):
        self.start_page = MainWindow()
        # 信号槽连接
        self.start_page.switch_contrast_ratio_window.connect(
            self.show_contrast_ratio_page)
        self.start_page.switch_smooth_sharp_window.connect(
            self.show_smooth_sharp_page)
        self.start_page.switch_fourier_window.connect(self.show_fourier_page)
        self.start_page.switch_noise_window.connect(self.show_noise_page)
        self.start_page.switch_edge_window.connect(self.show_edge_page)
        self.start_page.switch_bin_window.connect(self.show_bin_page)

        self.start_page.show()
    def show_bin_page(self):
        self.bin_page = Binary_Window()
        self.bin_page.switch_execute_img_pro.connect(self.save_img_bin)
        self.bin_page.switch_execute_img_pro.connect(self.send_img)
        self.bin_page.img_origin = self.start_page.img_origin
        self.bin_page.show()

    def show_contrast_ratio_page(self):
        self.contrast_ratio_page = Contrast_ratio_window()
        # 页面间传递图片
        self.contrast_ratio_page.switch_execute_img_pro.connect(
            self.save_img_contrast_ratio)
        self.contrast_ratio_page.switch_execute_img_pro.connect(self.send_img)

        # 唤起页面的时候必须将图片传递过去
        self.contrast_ratio_page.img_origin = self.start_page.img_origin
        self.contrast_ratio_page.show()

    def show_smooth_sharp_page(self):
        self.smooth_sharp_page = Smooth_sharp_window()
        # 页面间传递图片
        self.smooth_sharp_page.switch_execute_img_pro.connect(
            self.save_img_smooth_sharp)
        self.smooth_sharp_page.switch_execute_img_pro.connect(self.send_img)

        self.smooth_sharp_page.img_origin = self.start_page.img_origin
        self.smooth_sharp_page.show()

    def show_fourier_page(self):
        self.fourier_page = Fourier_window()
        # 页面间传递图片
        self.fourier_page.switch_execute_img_pro.connect(
            self.save_img_fourier)
        self.fourier_page.switch_execute_img_pro.connect(self.send_img)
        self.fourier_page.img_origin = self.start_page.img_origin
        self.fourier_page.show()

    def show_noise_page(self):
        self.noise_page = Noise_window()
        self.noise_page.switch_execute_img_pro.connect(self.save_img_noise)
        self.noise_page.switch_execute_img_pro.connect(self.send_img)
        self.noise_page.img_origin = self.start_page.img_origin
        self.noise_page.show()
    
    def show_edge_page(self):
        self.edge_page= Edge_window()
        self.edge_page.switch_execute_img_pro.connect(self.save_img_edge)
        self.edge_page.switch_execute_img_pro.connect(self.send_img)
        self.edge_page.img_origin = self.start_page.img_origin
        self.edge_page.show()

    def send_img(self):
        """子页面将处理后的图片传递到主页面，并要求主页面刷新
        """
        self.start_page.img = self.img
        self.start_page.show_image()

    def save_img_contrast_ratio(self):
        self.img = self.contrast_ratio_page.img

    def save_img_smooth_sharp(self):
        self.img = self.smooth_sharp_page.img

    def save_img_fourier(self):
        self.img = self.fourier_page.img

    def save_img_noise(self):
        self.img = self.noise_page.img

    def save_img_edge(self):
        self.img = self.edge_page.img
    def save_img_bin(self):
        self.img = self.bin_page.img


if __name__ == "__main__":
    # 检查./data文件目录是否存在，不存在则创建
    if not os.path.exists('./data'):
        os.mkdir('./data')
    
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_start_page()
    # QApplication.setStyle('Windows')
    sys.exit(app.exec_())
