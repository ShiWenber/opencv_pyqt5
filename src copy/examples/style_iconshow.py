import sys

from PyQt5.QtWidgets import QStyle, QApplication, QWidget, QTableWidgetItem
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
# from qt_forms.frm_icon import Ui_Form


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(643, 383)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cmbIcon = QtWidgets.QComboBox(Form)
        self.cmbIcon.setObjectName("cmbIcon")
        self.horizontalLayout.addWidget(self.cmbIcon)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 10)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Styles:"))

class FrmInquireWarp(QWidget):
    def __init__(self):
        super(FrmInquireWarp, self).__init__()
        self.ui = Ui_Form()
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_TrashIcon))
        self.ui.setupUi(self)
        self.setWindowTitle("icons")
        self.ui.cmbIcon.currentTextChanged.connect(self.__dis_data)
        styles=['WindowsVista','Windows','Motif','CDE']
        for style in styles:
            self.ui.cmbIcon.addItem(style)


    def __dis_data(self,style):
        QApplication.setStyle(style)
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(7)
        self.ui.tableWidget.setColumnCount(10)

        icon_index=0
        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                icon=QApplication.style().standardIcon(icon_index)
                item=QTableWidgetItem(icon,str(icon_index))
                self.ui.tableWidget.setItem(row,col,item);
                icon_index+=1
        # data = self.model.itemFromIndex(index)
        # try:
        #     dic_data = data.data(role=Qt.UserRole)
        #     if isinstance(dic_data, dict):
        #         plt.plot(dic_data['x'], dic_data['y'])
        #         plt.title('spectra data')
        #         plt.show()
        # except BaseException as ex:
        #     QMessageBox.information(self, '警告', '谱图打开出错' + str(ex), QMessageBox.Yes | QMessageBox.No, QMessageBox.No)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = FrmInquireWarp()
    myWin.show()
    sys.exit(app.exec_())

