# -*- coding: utf-8 -*-
import tkinter
from tkinter import messagebox
from PyQt5 import QtCore, QtGui, QtWidgets
from LoginController import LoginController

controller = LoginController()


class Ui_MainWindow(object):
    def btn_create_clicked(self):
        from Register import Ui_MainWindow
        
        QtWidgets.QApplication.activeWindow().close()

        self.Register = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.Register)
        self.Register.show()

    def btn_login_clicked(self):
        this_window = QtWidgets.QApplication.activeWindow()

        user = self.txt_user.text().strip()
        password = self.txt_password.text().strip()
        response = controller.login(user, password)

        if response == 'USER NOT FOUND':
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', 'O usuário informado não existe.')
            tkinter.Tk().destroy()
        elif response == 'WRONG PASSWORD':
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', 'Senha incorreta para o usuário informado')
            tkinter.Tk().destroy()
        else:
            from App import Ui_MainWindow
        
            this_window.close()

            self.App = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.App)
            self.App.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(430, 450)
        MainWindow.setWindowTitle('GERENCIADOR DE VOLUNTÁRIOS')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName('gridLayout')
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText('SEJA BEM-VINDO')
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName('label')
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btn_create = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_create.setFont(font)
        self.btn_create.setText('CRIAR USUÁRIO')
        self.btn_create.setObjectName('btn_create')
        self.gridLayout.addWidget(self.btn_create, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText('USUÁRIO')
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName('label_3')
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.txt_user = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_user.sizePolicy().hasHeightForWidth())
        self.txt_user.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_user.setFont(font)
        self.txt_user.setText('')
        self.txt_user.setObjectName('txt_user')
        self.gridLayout.addWidget(self.txt_user, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText('Insira o usuário e a senha para continuar')
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName('label_2')
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.txt_password = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_password.sizePolicy().hasHeightForWidth())
        self.txt_password.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_password.setFont(font)
        self.txt_password.setText('')
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setObjectName('txt_password')
        self.gridLayout.addWidget(self.txt_password, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setText('SENHA')
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName('label_4')
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_login.setText('ENTRAR')
        self.btn_login.setObjectName('btn_login')
        self.gridLayout.addWidget(self.btn_login, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.btn_create.clicked.connect(self.btn_create_clicked)
        self.btn_login.clicked.connect(self.btn_login_clicked)

        controller.create()
        controller.reset_status()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
