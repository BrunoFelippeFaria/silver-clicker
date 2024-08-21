from pynput.mouse import Controller, Button
from time import sleep

class AutoClicker:
    def __init__(self):
        #configurações 
        self.limiteCliques = True
        self.ativado = False
        self.delay = 5
        self.cliquesTotal = 15
        self.cliqueAtual = 0
        self.mouse = Controller()
    
    def clicker(self):
        self.cliqueAtual = 0
        sleep(0.5)
        while self.ativado:
            self.mouse.click(Button.left)
            self.cliqueAtual += 1
            if self.limiteCliques and self.cliqueAtual >= self.cliquesTotal:
                self.ativado = False
                
            sleep(self.delay)

