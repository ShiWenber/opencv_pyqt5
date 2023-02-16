"""
pyqt5 App for pm4py

author: boer
last edited: 2022-12-29
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QMenu, QPushButton
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAct = QAction(QApplication.style().standardIcon(44), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        impMenu = QMenu('Import', self)
        impAct = QAction(QApplication.style().standardIcon(21), 'Import csv', self)
        impAct2 = QAction(QApplication.style().standardIcon(21), 'Import xes', self)
        impMenu.addAction(impAct)
        impMenu.addAction(impAct2)

        newAct = QAction(QApplication.style().standardIcon(32), 'New', self)
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        dinerB = QPushButton('Diner', self)
        dinerB.move(50, 50)
        dinerB.clicked.connect(self.push_event)


        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')    
        self.show()

    def push_event(self):
        '''
        和dinerB绑定的函数
        '''
        print("button clicked")
      
if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setStyle('Windows')
    ex = Example()
    sys.exit(app.exec_())
