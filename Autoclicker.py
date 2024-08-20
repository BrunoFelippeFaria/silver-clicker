from pyautogui import click
from time import sleep

class AutoClicker:
    def __init__(self):
        #configurações 
        self.infcliques = False
        self.ativado = False
        self.delay = 5
        self.cliques = 15
    
    def mostrar_status(self):
        print("ativado: ", self.ativado)
        print("cliques: ", self.cliques)
    
    def clicker(self):
        while self.ativado:
            click()
            if not self.infcliques:
                self.cliques -= 1
                if self.cliques <= 0:
                    self.ativado = False
        sleep(self.delay)

