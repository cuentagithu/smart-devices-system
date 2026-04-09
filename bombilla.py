class BombillaInteligente:
    def __init__(self, color='blanco', estado='apagado'):
        self.color = color
        self.estado = estado

    def encender(self):
        self.estado = 'encendido'
        print(f'Bombilla encendida en color {self.color}.')

    def apagar(self):
        self.estado = 'apagado'
        print('Bombilla apagada.')

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        print(f'Color cambiado a {self.color}.')

    def obtener_estado(self):
        return self.estado
    
    def obtener_color(self):
        return self.color
