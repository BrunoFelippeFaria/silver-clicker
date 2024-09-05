from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QCheckBox, QTimeEdit, QDoubleSpinBox, QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton, QRadioButton, QSpinBox, QWidget, QDockWidget
from PySide6.QtUiTools import QUiLoader

_loader = QUiLoader()

class MainWindow(QMainWindow):       
    def __init__(self):
        super().__init__() 
        #carrega a interface
        self.ui = _loader.load("ui/autoclicker.ui")
        #outras janelas
        self.hotkeyWindow = hotkeyWindow(self)
        #widgets
        self.btnStart = self.ui.findChild(QPushButton, "btnStart")
        self.btnHotkey = self.ui.findChild(QPushButton, "btnHotkey")

        self.cbLimiteCliques = self.ui.findChild(QCheckBox, "cbLimiteCliques")
        self.cbClicarTempo = self.ui.findChild(QCheckBox, "cbClicarTempo")
        self.cbTravarMouse = self.ui.findChild(QCheckBox, "cbTravarMouse")
        self.cbMinimizar = self.ui.findChild(QCheckBox, "cbMinimizar")
        self.cbMaximizar = self.ui.findChild(QCheckBox, "cbMaximizar")

        self.rbEsquerdo = self.ui.findChild(QRadioButton, "rbEsquerdo")
        self.rbDireito = self.ui.findChild(QRadioButton, "rbDireito")

        self.sbCliques = self.ui.findChild(QSpinBox, "sbCliques")
        self.dbDelay = self.ui.findChild(QDoubleSpinBox, "dbDelay")

        self.teClicar = self.ui.findChild(QTimeEdit, "teClicar")
        self.teAtivo = self.ui.findChild(QTimeEdit, "teAtivo")


        self.img = self.ui.findChild(QLabel, "img")
        self.img.setPixmap(QPixmap("imagens/mouse.png"))

        #configs padrão dos widgets 
        self.dbDelay.setValue(1.0)
        self.sbCliques.setValue(15)
        self.cbLimiteCliques.setChecked(True)
        self.rbEsquerdo.setChecked(True)

        #configs da janela
        self.setCentralWidget(self.ui)
        self.resize(QSize(700,500))
        self.setWindowTitle("Silver Clicker")
        self.setWindowIcon(QPixmap("imagens/mouseIcon.png"))
        #eventos
        self.btnHotkey.clicked.connect(self.mostrarHotkeyWindow)


    def mostrarHotkeyWindow(self):
        self.hotkeyWindow.show()
    
    def mostrarErro(self, txt, infoTxt, titulo):
        MessageBox = QMessageBox()
        MessageBox.setIcon(QMessageBox.Critical)
        MessageBox.setText(txt)
        MessageBox.setInformativeText(infoTxt)
        MessageBox.setWindowTitle(titulo)
        return MessageBox

        

class hotkeyWindow(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.ui = _loader.load("ui/hotkey.ui", self)
        self.mainWindow = mainWindow
        #widgets
        self.btnOk = self.findChild(QPushButton,"btnOk")
        self.lineEdit = self.findChild(QLineEdit,"lineEdit")
        
        #eventos
        self.btnOk.clicked.connect(self.btnOkPress)

        #configs da janela
        self.setWindowTitle("hotkey")
    def btnOkPress(self):
        arquivo = open("atalho","w+")
        arquivo.write(self.lineEdit.text())
        arquivo.close()
        
    
    
