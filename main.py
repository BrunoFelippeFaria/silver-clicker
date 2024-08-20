import sys
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
        self.window.startBtn.clicked.connect(self.startBtnPress)
        app.exec()
    
    def startBtnPress(self):
        self.autoclicker.ativado = not self.autoclicker.ativado
        self.window.showMinimized()
        self.autoclicker.mostrar_status()
        self.autoclicker.clicker()
        if not self.autoclicker.ativado:
            self.window.startBtn.setText("start")
        else:
            self.window.startBtn.setText("stop")



if __name__ == "__main__":
    main = Main()
