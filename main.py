import sys
import threading
from PySide6.QtWidgets import QApplication
from Autoclicker import AutoClicker
from gui import MainWindow


class Main():
    def __init__(self):
        app = QApplication(sys.argv)
        self.autoclicker = AutoClicker()
        self.window = MainWindow()
        self.window.show()
        
        #eventos
        self.window.btnStart.clicked.connect(self.startClicker)
        app.exec()
    
    def atualizar(self):
       self.autoclicker.delay = self.window.dbDelay.value()
       self.autoclicker.limiteCliques = self.window.cbLimiteCliques.isChecked()

    def startClicker(self):
        self.atualizar()
        self.debug()
        self.autoclicker.ativado = not self.autoclicker.ativado
    
        if not self.autoclicker.ativado:
            self.window.btnStart.setText("iniciar")
        else:    
            if self.window.cbMinimizar.isChecked():
                self.window.showMinimized() 
            
            thread = threading.Thread(target=self.autoclicker.clicker)
            thread.start()
            self.window.btnStart.setText("parar")

       
    
    def debug(self):
        print("cliques: ", self.autoclicker.cliquesTotal)
        print("delay: ", self.autoclicker.delay)
        print("ativo ", self.autoclicker.ativado)
    


if __name__ == "__main__":
    main = Main()
