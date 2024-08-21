from PySide6.QtCore import QSize
from PySide6.QtWidgets import QCheckBox, QDoubleSpinBox, QLabel, QMainWindow, QPushButton, QRadioButton, QSpinBox
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
        self.btnStart = self.ui.findChild(QPushButton, "btnStart")
        self.btnHotkey = self.ui.findChild(QPushButton, "btnHotkey")
        
        self.cbLimiteCliques = self.ui.findChild(QCheckBox, "cbLimiteCliques")
        self.cbClicarTempo = self.ui.findChild(QCheckBox, "cbClicarTempo")
        self.cbBloquearMouse = self.ui.findChild(QCheckBox, "cbBloquearMouse")
        self.cbMinimizar = self.ui.findChild(QCheckBox, "cbMinimizar")
        self.cbMaximizar = self.ui.findChild(QCheckBox, "cbMaximizar")

        self.rbEsquerdo = self.ui.findChild(QRadioButton, "rbEsquerdo")
        self.rbDireito = self.ui.findChild(QRadioButton, "rbDireito")

        self.sbCliques = self.ui.findChild(QSpinBox, "sbCliques")
        self.dbDelay = self.ui.findChild(QDoubleSpinBox, "dbDelay")

        self.img = self.ui.findChild(QLabel, "img")

        #configs da janela
        self.setCentralWidget(self.ui)
        self.resize(QSize(700,500))
        self.setWindowTitle("Silver Clicker")
        
