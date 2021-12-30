from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QDialog
import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(302, 210)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 191))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.line_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_name.setObjectName("line_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_name)
        self.line_roast = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_roast.setObjectName("line_roast")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_roast)
        self.line_type = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_type.setObjectName("line_type")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_type)
        self.line_describe = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_describe.setObjectName("line_describe")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line_describe)
        self.line_price = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_price.setObjectName("line_price")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.line_price)
        self.line_mass = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_mass.setObjectName("line_mass")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.line_mass)
        self.button = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button.setFont(font)
        self.button.setObjectName("button")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "название"))
        self.label_2.setText(_translate("Dialog", "прожарка"))
        self.label_3.setText(_translate("Dialog", "тип"))
        self.label_4.setText(_translate("Dialog", "описание"))
        self.label_5.setText(_translate("Dialog", "цена"))
        self.label_6.setText(_translate("Dialog", "масса"))
        self.button.setText(_translate("Dialog", "Добавить"))


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, is_edit=False, _id=None):
        super(Dialog, self).__init__()
        self.setupUi(self)
        self.button.clicked.connect(self.add_coffee)
        self.is_edit = is_edit
        self._id = _id

    def add_coffee(self):
        n = self.line_name.text()
        r = self.line_roast.text()
        t = self.line_type.text()
        d = self.line_describe.text()
        p = self.line_price.text()
        m = self.line_mass.text()
        if self._id is None:
            with sqlite3.connect("coffee.sqlite") as db:
                cur = db.cursor()
                cur.execute(f"INSERT INTO coffee VALUES (NULL, '{n}', '{r}', '{t}', '{d}', {p}, {m})")
        else:
            with sqlite3.connect("coffee.sqlite") as db:
                cur = db.cursor()
                cur.execute(f"""UPDATE coffee SET name = '{n}', roasting = {r}, type = {t}, describe = {d},
                price = {p}, mass = {m} WHERE id == {self._id}""")
        self.close()


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setStyleSheet("background-color: rgb(255, 172, 247);")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(5, 24, 790, 571))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(10, 10, 10);")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.but_add_coffee = QtWidgets.QPushButton(Form)
        self.but_add_coffee.setGeometry(QtCore.QRect(0, 0, 400, 23))
        self.but_add_coffee.setStyleSheet("background-color: rgb(238, 229, 255);\n"
"color: rgb(63, 63, 63);")
        self.but_add_coffee.setObjectName("but_add_coffee")
        self.but_edit_coffee = QtWidgets.QPushButton(Form)
        self.but_edit_coffee.setGeometry(QtCore.QRect(400, 0, 400, 23))
        self.but_edit_coffee.setStyleSheet("background-color: rgb(238, 229, 255);\n"
"color: rgb(63, 63, 63);")
        self.but_edit_coffee.setObjectName("but_edit_coffee")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.but_add_coffee.setText(_translate("Form", "Добавить"))
        self.but_edit_coffee.setText(_translate("Form", "Редактировать"))


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(800, 600)
        self.show_table()
        self.but_add_coffee.clicked.connect(self.add_coffee)
        self.but_edit_coffee.clicked.connect(self.edit_coffee)

    def show_table(self):
        with sqlite3.connect("coffee.sqlite") as db:
            cur = db.cursor()
            headers_names = cur.execute("SELECT * FROM coffee").description
            self.tableWidget.setHorizontalHeaderLabels(([i[0] for i in headers_names]))
            self.tableWidget.setRowCount(0)
            res = cur.execute(f"SELECT * FROM coffee").fetchall()
            for i, row in enumerate(res):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

    def add_coffee(self):
        dialog = Dialog()
        dialog.show()
        dialog.exec_()
        self.show_table()

    def edit_coffee(self):
        try:
            rows = [i.row() for i in self.tableWidget.selectedItems()]
            dialog = Dialog(True, self.tableWidget.item(rows[0], 0).text())
            dialog.line_name.setText(self.tableWidget.item(rows[0], 1).text())
            dialog.line_roast.setText(self.tableWidget.item(rows[0], 2).text())
            dialog.line_type.setText(self.tableWidget.item(rows[0], 3).text())
            dialog.line_describe.setText(self.tableWidget.item(rows[0], 4).text())
            dialog.line_price.setText(self.tableWidget.item(rows[0], 5).text())
            dialog.line_mass.setText(self.tableWidget.item(rows[0], 6).text())
            dialog.show()
            dialog.exec_()
            self.show_table()
        except BaseException as er:
            print(er)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
