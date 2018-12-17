import json
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, \
    QMessageBox, QWidget, QGridLayout, \
    QVBoxLayout,  QApplication, QMainWindow, \
    QTextEdit, QLabel, QDesktopWidget, QPushButton, QSizePolicy


class ddh(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Создание главного окна
        x = (QDesktopWidget().screenGeometry().width() -
             QDesktopWidget().screenGeometry().width() // 2) // 2
        y = (QDesktopWidget().screenGeometry().height() -
             QDesktopWidget().screenGeometry().height() // 2) // 2
        self.setGeometry(x, y, QDesktopWidget().screenGeometry().width() / 2,
                         QDesktopWidget().screenGeometry().height() / 2)
        self.setObjectName('main_window')
        self.setWindowTitle('DDH')
        self.setStyleSheet('background: #fafafa;')

        # Создание виджета главного окна
        self.main_window_widget = QWidget(self)
        self.main_window_widget.setObjectName('main_window_widget')
        self.main_window_widget.setStyleSheet('background: #fafafa;')

        # Создание сетки главного окна
        self.main_window_grid = QGridLayout(self.main_window_widget)
        self.main_window_grid.setObjectName('main_window_grid')

        # Создание виджета для кнопок
        self.btn_widget = QWidget(self.main_window_widget)
        self.btn_widget.setObjectName('btn_widget')
        self.btn_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btn_widget.setMinimumSize(QtCore.QSize(300, 270))
        self.btn_widget.setMaximumSize(QtCore.QSize(300, 270))

        # Создание блока кнопок
        self.btn_block = QVBoxLayout(self.btn_widget)
        self.btn_block.setObjectName('btn_block')
        self.btn_block.setContentsMargins(50, 25, 50, 25)
        self.btn_block.setSpacing(35)

        # Создание кнопок для редактирования json файла
        btn_create_info = (('add', 'добавить', self.add_func),
                           ('change', 'изменить', self.change_func),
                           ('del', 'удалить', self.del_func),
                           ('exp', 'экспортировать', self.exp_func))
        for obj_name, name, btn_func in btn_create_info:
            self.btn = QPushButton(self.btn_widget)
            self.btn.setObjectName('btn_' + obj_name)
            self.btn.setText(name.upper())
            self.btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.btn.setMinimumSize(QtCore.QSize(200, 50))
            self.btn_block.addWidget(self.btn)
            self.btn.clicked.connect(btn_func)
        self.btn_widget.setStyleSheet('QPushButton {background: #212121; color: #fafafa;'
                                      'font-family: Arial Black; font-size: 10px;}')

        # Добавление сеток друг в друга
        self.main_window_grid.addWidget(self.btn_widget, 1, 1, 1, 1)
        self.setCentralWidget(self.main_window_widget)

    # Добавление функции в json файл
    def add_func(self):
        ans, ok_pressed = QInputDialog.getText(
            self, 'Добавить функцию', 'Введите название функции(без скобок)')
        if ok_pressed:
            self.file = open('data.json', 'w', encoding='utf8')
            data = dict()
            data[ans] = ''
            self.close()
            self.dialog = SecondWidget(ans)
            self.dialog.show()

    # Изменение существующей функции из json файла
    def change_func(self):
        ans, ok_pressed = QInputDialog.getText(
            self, 'Изменить функцию', 'Введите название функции(без скобок)')

    # Удаление функции из json файла
    def del_func(self):
        ans, ok_pressed = QInputDialog(self).getText(
            self, 'Удалить функцию', 'Введите название функции(без скобок)')

        try:
            with open('base.json', 'r', encoding='utf-8') as file:
                base = json.load(file)
                if ok_pressed:
                    del base[ans]

            with open('base.json', 'w+', encoding='utf-8') as file:
                json.dump(base, file)

            del_result_text = ('Удалено', 'Функция успешно удалена')

        except Exception:
            del_result_text = ('Ошибка', 'Функция не найдена')

        QMessageBox.information(self, *del_result_text)

    # Выбор формата для экспорта json файла
    def exp_func(self):
        ans, ok_pressed = QInputDialog.getItem(
            self, 'Экспортировать', 'Выберите формат экспорта',
            ('html', 'docs'), 0, False)


# Создание дополнительного окна для написания справки
class SecondWidget(QWidget):
    def __init__(self, ans):
        super().__init__()
        self.initUI(ans)

    def initUI(self, ans):
        self.n = 0

        self.ans = ans

        self.setObjectName('Form')
        self.resize(630, 633)
        self.setMaximumSize(QtCore.QSize(700, 700))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.gridcentral = QtWidgets.QGridLayout(self)
        self.gridcentral.setObjectName('gridcentral')
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMinimumSize(QtCore.QSize(612, 615))
        self.scrollArea.setMaximumSize(QtCore.QSize(690, 690))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName('scrollArea')
        self.scrollAreaWidgets = QtWidgets.QWidget()
        self.scrollAreaWidgets.setGeometry(QtCore.QRect(0, 0, 610, 613))
        self.scrollAreaWidgets.setObjectName('scrollAreaWidgets')
        self.gridscroll = QtWidgets.QGridLayout(self.scrollAreaWidgets)
        self.gridscroll.setObjectName('gridscroll')
        self.description = QLabel(self.scrollAreaWidgets)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.description.setFont(font)
        self.description.setObjectName('description')
        self.gridscroll.addWidget(self.description, 0, 0, 1, 1)
        self.description_textEdit = QTextEdit(self.scrollAreaWidgets)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.description_textEdit.setFont(font)
        self.description_textEdit.setObjectName('description_textEdit')
        self.gridscroll.addWidget(self.description_textEdit, 1, 0, 1, 1)
        self.syntax = QLabel(self.scrollAreaWidgets)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.syntax.setFont(font)
        self.syntax.setObjectName('syntax')
        self.gridscroll.addWidget(self.syntax, 2, 0, 1, 1)
        self.syntax_textEdit = QTextEdit(self.scrollAreaWidgets)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.syntax_textEdit.setFont(font)
        self.syntax_textEdit.setObjectName('syntax_textEdit')
        self.gridscroll.addWidget(self.syntax_textEdit, 3, 0, 1, 1)
        self.args = QLabel(self.scrollAreaWidgets)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.args.setFont(font)
        self.args.setObjectName('args')
        self.gridscroll.addWidget(self.args, 4, 0, 1, 1)
        self.add_args = QPushButton(self.scrollAreaWidgets)
        self.add_args.setMinimumSize(QtCore.QSize(0, 75))
        self.add_args.setMaximumSize(QtCore.QSize(150, 200))
        font = QtGui.QFont()
        font.setFamily('MS Shell Dlg 2')
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add_args.setFont(font)
        self.add_args.setObjectName('add_args')
        self.gridscroll.addWidget(self.add_args, 5, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgets)
        self.gridcentral.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.add_args.clicked.connect(self.add_arguments)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        screen = QDesktopWidget().showFullScreen()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


    def add_arguments(self):
        self.gridscroll.addWidget(self.add_args, self.n + 8, 0, 1, 1)
        self.gridargs = QtWidgets.QGridLayout()
        self.gridscroll.addLayout(self.gridargs, self.n + 7, 0, 1, 1)
        self.gridargs.setObjectName('gridargs_' + str(self.n))
        arg_info = (('Название аргумента', 'label_name_arg_', 'name_arg_textEdit_'),
                           ('Описаниее аргумента', 'label_description_arg_', 'description_arg_textEdit_'),
                           ('Тип аргумента', 'label_type_arg_', 'type_arg_textEdit_'),
                           ('Начальное значение аргумента', 'label_default_value_', 'default_value_textEdit_'),
                           ('Примечание', 'label_additions', 'additions_textEdit_'))
        self.just_line = QtWidgets.QFrame(self.scrollAreaWidgets)
        self.just_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.just_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridargs.addWidget(self.just_line, self.n + 6, 0, 1, 1)
        for name, label, textEdit in arg_info:
            self.gridarg = QtWidgets.QGridLayout()
            self.gridargs.addLayout(self.gridarg, self.n, 0, 1, 1)
            self.gridarg.setObjectName('gridargs_' + str(self.n))
            self.label_name_arg = QLabel(name, self.scrollAreaWidgets)
            self.label_name_arg.setObjectName(label + str(self.n))
            font = QtGui.QFont()
            font.setPointSize(16)
            self.label_name_arg.setFont(font)
            self.gridarg.addWidget(self.label_name_arg, self.n + 1, 0, 1, 1)
            self.name_arg_textEdit = QTextEdit(self.scrollAreaWidgets)
            self.name_arg_textEdit.setObjectName(textEdit + str(self.n))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.name_arg_textEdit.setFont(font)
            self.gridarg.addWidget(self.name_arg_textEdit, self.n + 2, 0, 1, 1)
            self.n += 1








    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate


        self.setWindowTitle(self.ans)
        self.description.setText(_translate('Form', 'Описание'))

        self.syntax.setText(_translate('Form', 'Синтакс'))

        self.args.setText(_translate('Form', 'Аргументы'))
        self.add_args.setText(_translate('Form', 'Добавить\n'
                                                 'аргумент'))



app = QApplication(sys.argv)
ex = ddh()
ex.show()
sys.exit(app.exec_())