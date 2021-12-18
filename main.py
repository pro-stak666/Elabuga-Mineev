from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem
from PyQt5 import uic
import sys
import sqlite3


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setFixedSize(800, 600)
        with sqlite3.connect("coffee.sqlite") as db:
            cur = db.cursor()
            headers_names = cur.execute("SELECT * FROM coffee").description
            self.tableWidget.setHorizontalHeaderLabels(([i[0] for i in headers_names]))

            res = cur.execute(f"SELECT * FROM coffee").fetchall()
            print(res)
            for i, row in enumerate(res):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
