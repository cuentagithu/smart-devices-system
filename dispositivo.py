from abc import ABC, abstractmethod

class Dispositivo(ABC):
    """
    Clase base abstracta para todos los dispositivos inteligentes.
    Define la interfaz común que todos los dispositivos deben implementar.
    """
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = False  # False = apagado, True = encendido
    
    def encender(self):
        """Enciende el dispositivo."""
        self.estado = True
        print(f"✓ {self.nombre} ha sido encendido")
    
    def apagar(self):
        """Apaga el dispositivo."""
        self.estado = False
        print(f"✗ {self.nombre} ha sido apagado")
    
    @abstractmethod
    def status(self):
        """Método polimórfico que muestra el estado del dispositivo."""
        pass
    
    @abstractmethod
    def configurar(self, *args, **kwargs):
        """Método sobrecargado para configuración del dispositivo."""
        pass
    
    def obtener_nombre(self):
        """Retorna el nombre del dispositivo."""
        return self.nombre
    
    def esta_encendido(self):
        """Retorna True si el dispositivo está encendido."""
        return self.estado
