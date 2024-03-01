import sys
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from main_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.listActor.addItems(["Châu Tinh Trì", "Trần Tiểu Xuân", "Khưu Thục Trinh", "Ngô Mẫn Đạt", "Trần Quán Hy", "Châu Nhuận Phát", "Lý Liên Kiệt", "Chu Ân"])
        self.ui.btnAdd.clicked.connect(self.addList)
        self.ui.btnInsert.clicked.connect(self.insertList)
        self.ui.btnEdit.clicked.connect(self.editList)
        self.ui.btnRemove.clicked.connect(self.removeList)
        self.ui.btnClear.clicked.connect(self.clearList)
        self.ui.btnSort.clicked.connect(self.sortList)
    
    def addList(self):
        text, ok = QInputDialog.getText(self, "Add a actor", "New actor:")
        if ok and text:
            self.ui.listActor.addItem(text)

    def insertList(self):
        text, ok = QInputDialog.getText(self, "Add a actor", "New actor:")
        if ok and text:
            currentRow = self.ui.listActor.currentRow()
            self.ui.listActor.insertItem(currentRow+1, text)

    def editList(self):
        currentRow = self.ui.listActor.currentRow()
        text, ok = QInputDialog.getText(self, "Add a actor", "New actor:", QLineEdit.Normal, self.ui.listActor.item(currentRow).text())
        if ok and text:
            self.ui.listActor.item(currentRow).setText(text)

    def removeList(self):
        currentRow = self.ui.listActor.currentRow()
        if currentRow >= 0:
            currentItem = self.ui.listActor.takeItem(currentRow)
            del currentItem

    def clearList(self):
        self.ui.listActor.clear()

    def sortList(self):
        self.ui.listActor.sortItems()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()