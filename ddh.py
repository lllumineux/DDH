import json
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, \
    QDesktopWidget, QMessageBox, QWidget, QGridLayout, QSizePolicy, \
    QVBoxLayout, QPushButton


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


app = QApplication(sys.argv)
ex = ddh()
ex.show()
sys.exit(app.exec_())
