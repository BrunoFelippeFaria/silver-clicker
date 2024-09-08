import sys
import json
from time import sleep, time
from threading import Thread
from PySide6.QtCore import QTime
from PySide6.QtWidgets import QApplication
from autoclicker import AutoClicker
from pynput import keyboard
from gui import MainWindow
from os.path import exists

class Main():
    def __init__(self):
        self.app = QApplication(sys.argv)
        #arquivo de configuração
        self.configFile = "config.json"
        self.config = None

        self.autoclicker = AutoClicker()
        self.window = MainWindow()
        self.window.show()
        self.atalhoIniciar = None
        self.listerner = None

        #configuração
        if (exists(self.configFile)):
            self.carregarConfig()
            self.config = self.getConfig()
        else:
            self.configsPadrao()
            self.config = self.getConfig()

        #eventos
        self.window.btnStart.clicked.connect(self.startClicker)
        self.window.atalhoWindow.btnOk.clicked.connect(self.atualizarAtalho)
        self.autoclicker.finished.connect(self.atualizarWindow)
        self.atualizarAtalho() 

        self.app.exec()

    def salvarConfig(self, config):
        with open(self.configFile, "w+") as file:
            json.dump(config, file, indent=4)
    
    def getConfig(self):
        with open(self.configFile, "r") as file:
            config = json.load(file)
            return config

    def carregarConfig(self):
        config = self.getConfig()
        self.window.dbDelay.setValue(config["delay"])
        self.window.sbCliques.setValue(config["cliques"])
        self.window.cbLimiteCliques.setChecked(config["limiteCliques"])
        self.window.cbClicarTempo.setChecked(config["clicarTempo"])
        self.window.cbTravarMouse.setChecked(config["travarMouse"])
        self.window.cbMinimizar.setChecked(config["minimizar"])
        self.window.cbMaximizar.setChecked(config["maximizar"])
        self.window.rbEsquerdo.setChecked(config["btnEsquerdo"])
    
    def atualizarConfig(self, config):
        config["delay"] = self.window.dbDelay.value()
        config["cliques"] = self.window.sbCliques.value()
        config["limiteCliques"] = self.window.cbLimiteCliques.isChecked()
        config["clicarTempo"] = self.window.cbClicarTempo.isChecked()
        config["travarMouse"] = self.window.cbTravarMouse.isChecked()
        config["minimizar"] = self.window.cbMinimizar.isChecked()
        config["maximizar"] = self.window.cbMaximizar.isChecked()
        config["btnEsquerdo"] = self.window.rbEsquerdo.isChecked()
        self.salvarConfig(config)

    def configsPadrao(self):
        config = {
            "delay": 1.0,
            "cliques": 15,
            "limiteCliques": True,
            "clicarTempo": False,
            "travarMouse": False,
            "minimizar": False,
            "maximizar": False,
            "btnEsquerdo": True,
            "atalho": "ctrl+shift+p"
        }
        self.salvarConfig(config)
        self.carregarConfig()

    def atualizarAtalho(self):        
        self.config = self.getConfig()
        if self.listerner:
            self.listerner.stop()
        
        atalhoStr = self.config["atalho"].strip().lower()
        
        keys = atalhoStr.split("+")
        formated_keys = []
        specialKeys = {"shift", "ctrl", "alt", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12", "tab"}

        for key in keys:
            if key in specialKeys:
                formated_keys.append(f"<{key}>")
            else:
                formated_keys.append(key)
            self.atalhoIniciar = "+".join(formated_keys)
    
        try:
            self.listerner = keyboard.GlobalHotKeys({
                self.atalhoIniciar: self.startClicker
            })
            self.listerner.start()
        except:
            erro = "atalho invalido"
            infotxt = "o texto inserido não pode ser usado como atalho"
            MessageBox = self.window.mostrarErro(erro, infotxt, erro)
            MessageBox.exec()
            self.config["atalho"] = "ctrl+shift+p"
            self.salvarConfig(self.config)
        else:
            if self.window.atalhoWindow.isVisible():
                self.window.atalhoWindow.close()

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

    def timer(self):
        inicio = time()
        while self.autoclicker.ativado:
            tempoExecucao = time() - inicio
            #converte o tempo para horas, minutos e segundos
            horas = int(tempoExecucao // 3600)
            minutos = int((tempoExecucao % 3600) // 60)
            segundos = int(tempoExecucao % 60)

            self.window.teAtivo.setTime(QTime(horas, minutos, segundos))

            tempoClicar = self.window.teClicar.time()
            tempoAtivo = self.window.teAtivo.time()

            if self.window.cbClicarTempo.isChecked() and tempoClicar == tempoAtivo:
                self.startClicker()

            sleep(0.1)

    def startClicker(self):
        self.atualizar()
        self.autoclicker.ativado = not self.autoclicker.ativado
        self.atualizarWindow()
        if self.autoclicker.ativado:
            thread = Thread(target=self.timer)
            thread.start()
            self.autoclicker.start()

    def atualizarWindow(self):
        if not self.autoclicker.ativado:
            if self.window.cbMaximizar.isChecked():
                self.window.showNormal()
                self.window.activateWindow()
            self.window.btnStart.setText("Iniciar")
        else:
            if self.window.cbMinimizar.isChecked():
                self.window.showMinimized()
            self.window.btnStart.setText("Parar")
            
    def closeEvent(self, event):
        if self.listerner:
            self.listerner.stop()
        event.accept()

if __name__ == "__main__":
    main = Main()
    main.atualizarConfig(main.config)

