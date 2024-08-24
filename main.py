import sys
from time import sleep
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import QApplication
from autoclicker import AutoClicker
from pynput import keyboard
from gui import MainWindow


class Main():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.autoclicker = AutoClicker()
        self.autoclicker.main = self
        self.window = MainWindow()
        self.window.show()
        self.startShortcut = None
        self.listerner = None

        #eventos
        self.window.btnStart.clicked.connect(self.startClicker)
        self.window.hotkeyWindow.btnOk.clicked.connect(self.atualizarAtalho)
        self.autoclicker.finished.connect(self.atualizarWindow)
        self.atualizarAtalho() 
        
        self.app.exec()

    def atualizarAtalho(self):
        if self.listerner:
            self.listerner.stop()
        with open("atalho", "r") as atalho:
            atalhoStr = atalho.read().strip()
            
            keys = atalhoStr.split("+")
            formated_keys = []

            for key in keys:
                if key in {"shift", "ctrl", "alt"}:
                    formated_keys.append(f"<{key}>")
                else:
                    formated_keys.append(key)
                self.startShortcut = "+".join(formated_keys)
        
            try:
                self.listerner = keyboard.GlobalHotKeys({
                    self.startShortcut: self.startClicker
                })
                self.listerner.start()
            except:
                erro = "atalho invalido"
                infotxt = "o texto inserido não pode ser usado como atalho"
                MessageBox = self.window.mostrarErro(erro, infotxt, erro)
                MessageBox.exec()
            else:
                if self.window.hotkeyWindow.isVisible():
                    self.window.hotkeyWindow.close()
    
    def on_press(self, key):
        if hasattr(key, "char") and key.char:
            char = key.char
            if char in self.startShortcut:
                self.startShortcut[char]()


    def atualizar(self):
       self.autoclicker.botaoEsquerdo = self.window.rbEsquerdo.isChecked()
       self.autoclicker.cliquesTotal = self.window.sbCliques.value() 
       self.autoclicker.delay = self.window.dbDelay.value()
       self.autoclicker.limiteCliques = self.window.cbLimiteCliques.isChecked()
       self.autoclicker.travarMouse = self.window.cbTravarMouse.isChecked()

    def startClicker(self):
        self.atualizar()
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
            
    def closeEvent(self, event):
        if self.listerner:
            self.listerner.stop()
        event.accept()
    
    def debug(self):
        print("cliques: ", self.autoclicker.cliquesTotal)
        print("delay: ", self.autoclicker.delay)
        print("ativo ", self.autoclicker.ativado)
    


if __name__ == "__main__":
    main = Main()
