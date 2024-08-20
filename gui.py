from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QPushButton
from PySide6.QtUiTools import QUiLoader 


_loader = QUiLoader()

class MainWindow(QMainWindow):       
    def __init__(self):
        super().__init__() 
        #carrega a interface
        self.ui = _loader.load("autoclicker.ui")
        #menubar
        self.menuBar().addMenu("autoclicker")
        self.menuBar().addMenu("configurações")
        self.menuBar().addMenu("sobre")
        #widgets
        self.startBtn = self.ui.findChild(QPushButton, "btnStart")

        #configs da janela
        self.setCentralWidget(self.ui)
        self.resize(QSize(700,500))
        self.setWindowTitle("autoclicker")

