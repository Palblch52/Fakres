from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QTableWidget,QTableWidgetItem

import sys
from library import*

app = QtWidgets.QApplication([])
win = uic.loadUi("employee.ui")

Gr = Grup()
Gr.read_data("text.txt")

def btnLoadTable():
    win.tableWidget.setRowCount(Gr.count)
    row = 0
    for x in Gr.A:

        win.tableWidget.setItem(row, 0, QTableWidgetItem(Gr.A[x].fam+' '+Gr.A[x].name+' '+Gr.A[x].surname))
        win.tableWidget.setItem(row, 1, QTableWidgetItem(Gr.A[x].division))
        win.tableWidget.setItem(row, 2, QTableWidgetItem(Gr.A[x].days))
        win.tableWidget.setItem(row, 3, QTableWidgetItem(Gr.A[x].salary))
        row += 1
    
def btnAppendEmployee():
    strEmployee = win.lineEdit.text()

    Gr.appendEmployee(strEmployee)
    win.lineEdit.clear()
    win.tableWidget.clear()
    btnLoadTable()

    
win.pushButton.clicked.connect(btnLoadTable)

win.pushButton_3.clicked.connect(btnAppendEmployee)

win.show()
sys.exit(app.exec())