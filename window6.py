# Form implementation generated from reading ui file 'window6.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_window6(object):
    def setupUi(self, window6):
        window6.setObjectName("window6")
        window6.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=window6)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 142, 782, 135))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 425, 782, 135))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_6.addWidget(self.pushButton_6)
        self.frame_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 782, 136))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_7.addWidget(self.pushButton_7)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 283, 782, 136))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_8.addWidget(self.pushButton_8)
        window6.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=window6)
        self.statusbar.setObjectName("statusbar")
        window6.setStatusBar(self.statusbar)

        self.retranslateUi(window6)
        QtCore.QMetaObject.connectSlotsByName(window6)

    def retranslateUi(self, window6):
        _translate = QtCore.QCoreApplication.translate
        window6.setWindowTitle(_translate("window6", "window6"))
        self.pushButton_5.setText(_translate("window6", "WHATSAPP CHATS"))
        self.pushButton_6.setText(_translate("window6", "FOLDERS"))
        self.pushButton_7.setText(_translate("window6", "LOG FILE"))
        self.pushButton_8.setText(_translate("window6", "EMAILS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window6 = QtWidgets.QMainWindow()
    ui = Ui_window6()
    ui.setupUi(window6)
    window6.show()
    sys.exit(app.exec())