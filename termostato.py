class TermostatoInteligente:
    def __init__(self, temperatura_inicial=20.0):
        self.temperatura = temperatura_inicial
        self.estado = 'apagado'

    def encender(self):
        self.estado = 'encendido'
        print("Termostato encendido.")

    def apagar(self):
        self.estado = 'apagado'
        print("Termostato apagado.")

    def ajustar_temperatura(self, nueva_temperatura):
        self.temperatura = nueva_temperatura
        print(f"Temperatura ajustada a {self.temperatura} grados.")

    def obtener_estado(self):
        return self.estado

    def obtener_temperatura(self):
        return self.temperatura