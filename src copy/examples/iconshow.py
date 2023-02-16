# 显示所有的图标及器索引
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWnd(QWidget):
    def __init__(self, parent=None):
        super(MainWnd, self).__init__(parent)
        icons = sorted(self.getEnumStrings(QStyle, QStyle.StandardPixmap).items())
        layout = QGridLayout(self)
        colNums = 4 # 每行显示的图标数量
        for i, iconInfo in enumerate(icons[1:]):
            btn = QPushButton(QApplication.style().standardIcon(i), '{}-{}'.format(*iconInfo))
            btn.setStyleSheet('QPushButton{text-align:left;height:30}')
            layout.addWidget(btn, i // colNums, i % colNums)
            self.setWindowTitle('QStyle StandardPixmap')
            self.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_DriverFDIcon))
    def getEnumStrings(self, cls, enum):
        s = {}
        for key in dir(cls):
            value = getattr(cls, key)
            if isinstance(value, enum):
                s['{:02d}'.format(value)] = key
                return s


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWnd = MainWnd()
    mainWnd.show()
    sys.exit(app.exec_())

