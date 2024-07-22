from PyQt5 import Qt
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

        win.tableWidget.setItem(row, 0, QTableWidgetItem(Gr.A[x].fam))
        win.tableWidget.setItem(row, 1, QTableWidgetItem(Gr.A[x].name))
        win.tableWidget.setItem(row, 2, QTableWidgetItem(Gr.A[x].surname))
        win.tableWidget.setItem(row, 3, QTableWidgetItem(Gr.A[x].division))
        win.tableWidget.setItem(row, 4, QTableWidgetItem(Gr.A[x].days))
        win.tableWidget.setItem(row, 5, QTableWidgetItem(Gr.A[x].salary))
        row += 1
    
def btnAppendEmployee():
    List = [str(win.lineEdit_4.text()),str(win.lineEdit_5.text()),str(win.lineEdit_6.text()),\
            str(win.lineEdit_7.text()),str(win.lineEdit_8.text()),str(win.lineEdit_9.text())]

    Gr.appendEmployee(List)

    win.tableWidget.clear()
    btnLoadTable()

def btnEditEmployee():
    if win.lineEdit_2.text() == '' :
        win.lineEdit_2.setText('1')

    if win.lineEdit_3.text() == '':    
        win.lineEdit_3.setText('1')
    
    x = int(win.lineEdit_2.text())-1
    y = int(win.lineEdit_3.text())-1

    if x <= win.tableWidget.rowCount() and y <= win.tableWidget.columnCount(): 
         
        List = [str(win.tableWidget.item(x,0).text()),\
            str(win.tableWidget.item(x,1).text()),\
            str(win.tableWidget.item(x,2).text()),\
            str(win.tableWidget.item(x,3).text()),\
            str(win.tableWidget.item(x,4).text()),\
            str(win.tableWidget.item(x,5).text())]
   
        key = Gr.find_keyEmployee(List)
         
        if key != -1 :

            win.tableWidget.setItem(x,y,QTableWidgetItem(str(win.lineEdit.text())))

            List = [str(win.tableWidget.item(x,0).text()),\
            str(win.tableWidget.item(x,1).text()),\
            str(win.tableWidget.item(x,2).text()),\
            str(win.tableWidget.item(x,3).text()),\
            str(win.tableWidget.item(x,4).text()),\
            str(win.tableWidget.item(x,5).text()),]
             
            print(List)     
            Gr.editEmployee( key,List )

def btnDelEmployee():
    
    List = [str(win.lineEdit_4.text()),str(win.lineEdit_5.text()),str(win.lineEdit_6.text()),\
            str(win.lineEdit_7.text()),str(win.lineEdit_8.text()),str(win.lineEdit_9.text())]

    Gr.delEmployee(List)
  
    win.tableWidget.clear()
    
    btnLoadTable()
    
win.pushButton.clicked.connect(btnLoadTable)
win.pushButton_3.clicked.connect(btnAppendEmployee)
win.pushButton_4.clicked.connect(btnEditEmployee)
win.pushButton_5.clicked.connect(btnDelEmployee)   

win.show()
sys.exit(app.exec())