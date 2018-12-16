import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QInputDialog, \
    QTextEdit, QLabel, QDesktopWidget


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(898, 664)
        self.setStyleSheet("background:#fafafa;")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setStyleSheet("background: #fafafa;")
        self.centralwidget.setObjectName("centralwidget")
        self.grid = QtWidgets.QGridLayout(self.centralwidget)
        self.grid.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setSpacing(0)
        self.grid.setObjectName("grid")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(300, 270))
        self.widget.setMaximumSize(QtCore.QSize(300, 270))
        self.widget.setStyleSheet("background:#fafafa;")
        self.widget.setObjectName("widget")
        self.vLayout = QtWidgets.QVBoxLayout(self.widget)
        self.vLayout.setContentsMargins(50, 25, 50, 25)
        self.vLayout.setSpacing(35)
        self.vLayout.setObjectName("vLayout")
        self.btn_add_change = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_change.sizePolicy().hasHeightForWidth())
        self.btn_add_change.setSizePolicy(sizePolicy)
        self.btn_add_change.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        self.btn_add_change.setFont(font)
        self.btn_add_change.setStyleSheet("background: #040404; color: #fff;")
        self.btn_add_change.setObjectName("btn_add_change")
        self.vLayout.addWidget(self.btn_add_change)
        self.btn_delete = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy)
        self.btn_delete.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet("background: #040404; color: #fff;")
        self.btn_delete.setObjectName("btn_delete")
        self.vLayout.addWidget(self.btn_delete)
        self.btn_export = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_export.sizePolicy().hasHeightForWidth())
        self.btn_export.setSizePolicy(sizePolicy)
        self.btn_export.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        self.btn_export.setFont(font)
        self.btn_export.setStyleSheet("background: #040404; color: #fff;")
        self.btn_export.setObjectName("btn_export")
        self.vLayout.addWidget(self.btn_export)
        self.grid.addWidget(self.widget, 1, 1, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.btn_add_change.clicked.connect(self.add_change_function)

        self.btn_delete.clicked.connect(self.delete_function)

        self.btn_export.clicked.connect(self.export)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("DDH", "DDH"))
        self.btn_add_change.setText(_translate("DDH", "ДОБАВИТЬ / ИЗМЕНИТЬ"))
        self.btn_delete.setText(_translate("DDH", "УДАЛИТЬ"))
        self.btn_export.setText(_translate("DDH", "ЭКСПОРТИРОВАТЬ"))
    def export(self):
        ans, okPress = QInputDialog.getItem(self, 'Выбирете', 'Выбирете в какой формат вы хотите экспортировать', ("html", "word"), 0, False)


    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        screen = QDesktopWidget().showFullScreen()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def delete_function(self):
        ans, okPress = QInputDialog(self).getText(self, 'Удалить функцию', 'Введите название функции')



    def add_change_function(self):
        ans, okPress = QInputDialog.getText(self, 'Добавить функцию', 'Введите название функции')



app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())