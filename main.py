import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import QApplication
from Autoclicker import AutoClicker
from gui import MainWindow


class Main():
    def __init__(self):
        app = QApplication(sys.argv)
        self.autoclicker = AutoClicker()
        self.autoclicker.main = self
        self.window = MainWindow()
        self.window.show()
        self.startShortcut = None

        #eventos
        self.window.btnStart.clicked.connect(self.startClicker)
        self.window.hotkeyWindow.btnOk.clicked.connect(self.atualizarAtalho)
        self.autoclicker.finished.connect(self.atualizarWindow)
        self.atualizarAtalho() 
        app.exec()

    def atualizarAtalho(self):
        if self.startShortcut:
            self.startShortcut.setEnabled(False)
            self.startShortcut.deleteLater()
        with open("atalho", "r") as atalho:
            self.startShortcut = QShortcut(QKeySequence(atalho.read().strip()), self.window)
        self.startShortcut.activated.connect(self.startClicker) 
        

    def atualizar(self):
       self.autoclicker.botaoEsquerdo = self.window.rbEsquerdo.isChecked()
       self.autoclicker.cliquesTotal = self.window.sbCliques.value() 
       self.autoclicker.delay = self.window.dbDelay.value()
       self.autoclicker.limiteCliques = self.window.cbLimiteCliques.isChecked()

    def startClicker(self):
        self.atualizar()
        self.debug()
        self.autoclicker.ativado = not self.autoclicker.ativado
    
        self.atualizarWindow()
        
        if self.autoclicker.ativado: 
            self.autoclicker.start()

    def atualizarWindow(self):
        if not self.autoclicker.ativado:
            if self.window.cbMaximizar.isChecked():
                self.window.setWindowState(Qt.WindowNoState)
                self.window.activateWindow()
            self.window.btnStart.setText("iniciar")
        else:
            if self.window.cbMinimizar.isChecked():
                self.window.showMinimized()
            self.window.btnStart.setText("parar")
            
    
    def debug(self):
        print("cliques: ", self.autoclicker.cliquesTotal)
        print("delay: ", self.autoclicker.delay)
        print("ativo ", self.autoclicker.ativado)
    


if __name__ == "__main__":
    main = Main()
