from PySide6.QtCore import QThread, Signal
from pynput import mouse
from pynput.mouse import Controller, Button
from time import sleep

class AutoClicker(QThread):
    def __init__(self):
        super().__init__()
        finished = Signal()
        #configurações 
        self.limiteCliques = True
        self.ativado = False
        self.delay = 5
        self.cliquesTotal = 15
        self.cliqueAtual = 0
        self.mouse = Controller()
        self.botaoEsquerdo = True
        self.travarMouse = False
        
    def click(self):
        if self.botaoEsquerdo:
            self.mouse.click(Button.left)
        else:
            self.mouse.click(Button.right)

    def run(self):
        self.cliqueAtual = 0
        sleep(0.5)
        mousePos = self.mouse.position

        while self.ativado:
            if (self.travarMouse):
                self.mouse.position = (mousePos[0], mousePos[1])
            self.click()
            self.cliqueAtual += 1
            if self.limiteCliques and self.cliqueAtual >= self.cliquesTotal: 
                self.ativado = False
            
            sleep(self.delay)
        self.finished.emit()

