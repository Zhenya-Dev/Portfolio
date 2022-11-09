from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QMenuBar,QMenu,QFileDialog,QMessageBox

from time import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.font_size=14
        self.list_fonts={}
        self.List_fonts=[]


        self.setWindowTitle("Text editor")
        self.setGeometry(300,250,350,200)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.text = QtWidgets.QLabel()
        self.text.setText("")
        self.text.move(120, 100)

        self.createMenuBar()

    def createMenuBar(self): # menu creation
        self.menuBar=QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu("&File",self) #Creating a Menu Window
        self.menuBar.addMenu(fileMenu)

        labelbar = QMenu("&Size", self)
        self.menuBar.addMenu(labelbar)

        difbar=QMenu("&Width",self)
        self.menuBar.addMenu(difbar)

        fontbar = QMenu("&Font", self)
        self.menuBar.addMenu(fontbar)

        Time = QMenu("&Time", self)
        self.menuBar.addMenu(Time)

        Info = QMenu("&About", self)
        self.menuBar.addMenu(Info)




        fileMenu.addAction('Open',self.action_clicked)#creation of inscriptions
        fileMenu.addAction('Save',self.action_clicked)
        fileMenu.addAction("Create",self.action_clicked)

        for i in range(2,81,2):
            labelbar.addAction(str(i), self.text_clicked)

        self.list_fonts={"Ultra thin":QtGui.QFont.Thin,"Thin":QtGui.QFont.Light,
        "Medium":QtGui.QFont.Medium,"Bold":QtGui.QFont.Bold,"Ultra Bold":QtGui.QFont.Black}
        for j in self.list_fonts.keys():
            difbar.addAction(j,self.set_choice)

        self.List_fonts=['Arial','Bahnschrift','Bookman Old Style','Calibri','Comic Sans MS',
                    'Courier New','Ink Free','Javanese Text','MV Boli','Myanmar Text','Verdana',]
        for k in self.List_fonts:
            fontbar.addAction(k,self.font_choice)

        Info.addAction('About',self.info_prog)

        Time.addAction('Time',self.time_prog)








    @QtCore.pyqtSlot()
    def action_clicked(self):
        action=self.sender()
        if action.text()=="Open":#сделай в начале просто print для проверки
            fname = QFileDialog.getOpenFileName(self)[0]#если записать getOpenFileNames то откроет несколько файлов
            try:
                f=open(fname,"r")
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
            except FileNotFoundError:
                self.text.setText("File not found")
        elif action.text()=="Save":
            fname=QFileDialog.getSaveFileName()[0]

            try:
                f=open(fname,"w")
                text=self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                self.text.setText("File not found")
        elif action.text()=="Create":
            with open("new_file.txt", "w"):
                self.text.setText("File not found")

    @QtCore.pyqtSlot()
    def text_clicked(self):
        action=self.sender()
        self.font_size=int(action.text())
        self.text_edit.setFont(QtGui.QFont(self.List_fonts[0], self.font_size, self.list_fonts["Bold"]))

    @QtCore.pyqtSlot()
    def set_choice(self):
        action = self.sender()
        self.text_edit.setFont(QtGui.QFont(self.List_fonts[0], self.font_size, self.list_fonts[str(action.text())]))

    @QtCore.pyqtSlot()
    def font_choice(self):
        action = self.sender()
        self.text_edit.setFont(QtGui.QFont(action.text(), self.font_size, self.list_fonts["Bold"]))

    @QtCore.pyqtSlot()
    def info_prog(self):
        action = self.sender()
        info = QMessageBox()
        info.setIcon(QMessageBox.Information)
        info.setWindowTitle(action.text())
        if action.text()=="About":
            info.setText("Info about this text editor")
            info.setDetailedText('''This beautiful text editor was invented in order to
you enjoyed life, and did not clog your beautiful memory with unnecessary garbage
and wrote their important messages first here and then only in chats with people important to you''')
        info.exec()

    def time_prog(self):
        self.text_edit.setText(asctime())

















def application():
    app=QApplication(sys.argv)
    window=Window()

    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    application()