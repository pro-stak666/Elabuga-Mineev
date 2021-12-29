from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QDialog
from PyQt5 import uic
import sys
import sqlite3


class Dialog(QDialog):
    def __init__(self, is_edit=False, _id=None):
        super(Dialog, self).__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
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


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
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
